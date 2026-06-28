from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

LOG_PATH = (
    Path.home()
    / ".local"
    / "state"
    / "interview-prep-router"
    / "usage.jsonl"
)


def load_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []

    records: list[dict[str, Any]] = []

    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                print(
                    f"Skipping invalid JSON on line {line_number}",
                    file=sys.stderr,
                )

    return records


def split_records(
    records: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    requests: dict[str, dict[str, Any]] = {}
    feedback: dict[str, dict[str, Any]] = {}

    for record in records:
        if record.get("record_type") == "feedback":
            target_id = record.get("target_request_id")
            if target_id:
                feedback[target_id] = record
            continue

        request_id = record.get("request_id")
        if request_id:
            requests[request_id] = record

    ordered_requests = sorted(
        requests.values(),
        key=lambda item: item.get("timestamp", ""),
        reverse=True,
    )

    return ordered_requests, feedback


class MetricCard(QWidget):
    def __init__(self, title: str) -> None:
        super().__init__()

        self.title_label = QLabel(title)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.value_label = QLabel("0")
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value_label.setStyleSheet(
            "font-size: 22px; font-weight: bold;"
        )

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)

        self.setStyleSheet(
            """
            MetricCard {
                border: 1px solid palette(mid);
                border-radius: 8px;
                padding: 8px;
            }
            """
        )

    def set_value(self, value: str) -> None:
        self.value_label.setText(value)


class DashboardWindow(QMainWindow):
    COLUMNS = [
        "Time",
        "Backend",
        "Reason",
        "Prompt",
        "Completion",
        "Total",
        "Latency",
        "Feedback",
        "Claude Cost",
        "Avoided Cost",
    ]

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Interview AI Dashboard")
        self.resize(1250, 720)

        self.last_log_mtime_ns: int | None = None

        root = QWidget()
        root_layout = QVBoxLayout(root)

        metrics_layout = QGridLayout()

        self.total_card = MetricCard("Total requests")
        self.local_card = MetricCard("Local requests")
        self.claude_card = MetricCard("Claude requests")
        self.accepted_card = MetricCard("Accepted local")
        self.spend_card = MetricCard("Estimated Claude spend")
        self.savings_card = MetricCard("Accepted local savings")

        cards = [
            self.total_card,
            self.local_card,
            self.claude_card,
            self.accepted_card,
            self.spend_card,
            self.savings_card,
        ]

        for index, card in enumerate(cards):
            metrics_layout.addWidget(card, index // 3, index % 3)

        root_layout.addLayout(metrics_layout)

        self.status_label = QLabel(f"Log: {LOG_PATH}")
        root_layout.addWidget(self.status_label)

        self.table = QTableWidget()
        self.table.setColumnCount(len(self.COLUMNS))
        self.table.setHorizontalHeaderLabels(self.COLUMNS)
        self.table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )
        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.table.setAlternatingRowColors(True)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )
        header.setStretchLastSection(True)

        root_layout.addWidget(self.table)

        refresh_button = QPushButton("Refresh now")
        refresh_button.clicked.connect(self.refresh)
        root_layout.addWidget(refresh_button)

        self.setCentralWidget(root)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_if_changed)
        self.timer.start(1000)

        self.refresh()

    def refresh_if_changed(self) -> None:
        if not LOG_PATH.exists():
            if self.last_log_mtime_ns is not None:
                self.refresh()
            return

        current_mtime_ns = LOG_PATH.stat().st_mtime_ns

        if current_mtime_ns != self.last_log_mtime_ns:
            self.refresh()

    def refresh(self) -> None:
        try:
            records = load_records(LOG_PATH)
            requests, feedback = split_records(records)
            self.populate_metrics(requests, feedback)
            self.populate_table(requests, feedback)

            if LOG_PATH.exists():
                self.last_log_mtime_ns = LOG_PATH.stat().st_mtime_ns

            self.status_label.setText(
                f"Loaded {len(requests)} requests from {LOG_PATH}"
            )
        except OSError as exc:
            QMessageBox.critical(
                self,
                "Log read error",
                str(exc),
            )

    def populate_metrics(
        self,
        requests: list[dict[str, Any]],
        feedback: dict[str, dict[str, Any]],
    ) -> None:
        successful = [
            request
            for request in requests
            if request.get("success") is True
        ]

        route_counts = Counter(
            request.get("route", "unknown")
            for request in successful
        )

        accepted_local = [
            request
            for request in successful
            if request.get("route") == "interview-local"
            and feedback.get(
                request.get("request_id", ""),
                {},
            ).get("status") == "accepted"
        ]

        claude_spend = sum(
            float(
                request.get(
                    "actual_claude_cost_usd_estimate",
                    0,
                )
            )
            for request in successful
        )

        accepted_savings = sum(
            float(
                request.get(
                    "avoided_claude_cost_usd_estimate",
                    0,
                )
            )
            for request in accepted_local
        )

        self.total_card.set_value(str(len(successful)))
        self.local_card.set_value(
            str(route_counts.get("interview-local", 0))
        )
        self.claude_card.set_value(
            str(route_counts.get("interview-claude", 0))
        )
        self.accepted_card.set_value(str(len(accepted_local)))
        self.spend_card.set_value(f"${claude_spend:.6f}")
        self.savings_card.set_value(f"${accepted_savings:.6f}")

    def populate_table(
        self,
        requests: list[dict[str, Any]],
        feedback: dict[str, dict[str, Any]],
    ) -> None:
        self.table.setRowCount(len(requests))

        for row, request in enumerate(requests):
            request_id = request.get("request_id", "")
            feedback_status = feedback.get(
                request_id,
                {},
            ).get("status", "unreviewed")

            values = [
                request.get("timestamp", ""),
                request.get("route", ""),
                request.get("reason", ""),
                str(request.get("prompt_tokens", 0)),
                str(request.get("completion_tokens", 0)),
                str(request.get("total_tokens", 0)),
                f"{float(request.get('latency_seconds', 0)):.3f}s",
                feedback_status,
                (
                    "$"
                    f"{float(request.get('actual_claude_cost_usd_estimate', 0)):.6f}"
                ),
                (
                    "$"
                    f"{float(request.get('avoided_claude_cost_usd_estimate', 0)):.6f}"
                ),
            ]

            for column, value in enumerate(values):
                item = QTableWidgetItem(value)

                if column in {3, 4, 5, 6, 8, 9}:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignRight
                        | Qt.AlignmentFlag.AlignVCenter
                    )

                self.table.setItem(row, column, item)


def main() -> int:
    application = QApplication(sys.argv)
    application.setApplicationName("Interview AI Dashboard")

    window = DashboardWindow()
    window.show()

    return application.exec()


if __name__ == "__main__":
    raise SystemExit(main())
