from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QInputDialog,
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

        controls_layout = QHBoxLayout()

        self.accept_button = QPushButton("Mark accepted")
        self.accept_button.clicked.connect(
            lambda: self.record_feedback("accepted")
        )
        controls_layout.addWidget(self.accept_button)

        self.reject_button = QPushButton("Mark rejected")
        self.reject_button.clicked.connect(
            lambda: self.record_feedback("rejected")
        )
        controls_layout.addWidget(self.reject_button)

        refresh_button = QPushButton("Refresh now")
        refresh_button.clicked.connect(self.refresh)
        controls_layout.addWidget(refresh_button)

        controls_layout.addStretch()
        root_layout.addLayout(controls_layout)

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

                if column == 0:
                    item.setData(
                        Qt.ItemDataRole.UserRole,
                        request_id,
                    )

                if column in {3, 4, 5, 6, 8, 9}:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignRight
                        | Qt.AlignmentFlag.AlignVCenter
                    )

                if feedback_status == "accepted":
                    item.setBackground(QColor(220, 245, 225))
                elif feedback_status == "rejected":
                    item.setBackground(QColor(250, 225, 225))

                self.table.setItem(row, column, item)


    def selected_request(
        self,
    ) -> tuple[str, dict[str, Any]] | None:
        selected_rows = self.table.selectionModel().selectedRows()

        if len(selected_rows) != 1:
            QMessageBox.information(
                self,
                "Select one request",
                "Select exactly one request row first.",
            )
            return None

        row = selected_rows[0].row()
        first_item = self.table.item(row, 0)

        if first_item is None:
            return None

        request_id = first_item.data(Qt.ItemDataRole.UserRole)

        if not request_id:
            QMessageBox.warning(
                self,
                "Request ID missing",
                "The selected row does not contain a request ID.",
            )
            return None

        records = load_records(LOG_PATH)
        requests, _ = split_records(records)

        request = next(
            (
                item
                for item in requests
                if item.get("request_id") == request_id
            ),
            None,
        )

        if request is None:
            QMessageBox.warning(
                self,
                "Request not found",
                "The selected request is no longer present in the log.",
            )
            return None

        return str(request_id), request

    def record_feedback(self, status: str) -> None:
        selected = self.selected_request()

        if selected is None:
            return

        request_id, request = selected

        records = load_records(LOG_PATH)
        _, existing_feedback = split_records(records)
        current_feedback = existing_feedback.get(request_id)

        if current_feedback is not None:
            current_status = current_feedback.get(
                "status",
                "unknown",
            )
            current_reason = current_feedback.get(
                "reason",
                "",
            )

            message = (
                "This request already has feedback.\n\n"
                f"Current status: {current_status}\n"
                f"Current reason: {current_reason or '(none)'}\n\n"
                f"Replace it with '{status}' feedback?"
            )

            confirmation = QMessageBox.question(
                self,
                "Replace existing feedback?",
                message,
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )

            if confirmation != QMessageBox.StandardButton.Yes:
                return

        prompt = (
            "Why was this result accepted?"
            if status == "accepted"
            else "Why was this result rejected?"
        )

        reason, confirmed = QInputDialog.getText(
            self,
            f"Mark {status}",
            prompt,
        )

        if not confirmed:
            return

        reason = reason.strip()

        if not reason:
            QMessageBox.information(
                self,
                "Reason required",
                "Enter a short reason so the feedback remains useful.",
            )
            return

        feedback = {
            "record_type": "feedback",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "target_request_id": request_id,
            "status": status,
            "reason": reason,
            "route": request.get("route"),
            "routing_reason": request.get("reason"),
            "prompt_tokens": request.get("prompt_tokens", 0),
            "completion_tokens": request.get(
                "completion_tokens",
                0,
            ),
            "actual_claude_cost_usd_estimate": request.get(
                "actual_claude_cost_usd_estimate",
                0,
            ),
            "avoided_claude_cost_usd_estimate": request.get(
                "avoided_claude_cost_usd_estimate",
                0,
            ),
        }

        try:
            LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

            with LOG_PATH.open("a", encoding="utf-8") as handle:
                handle.write(
                    json.dumps(feedback, ensure_ascii=False)
                    + "\n"
                )
        except OSError as exc:
            QMessageBox.critical(
                self,
                "Feedback write error",
                str(exc),
            )
            return

        self.refresh()

        QMessageBox.information(
            self,
            "Feedback recorded",
            f"Request marked {status}.",
        )


def main() -> int:
    application = QApplication(sys.argv)
    application.setApplicationName("Interview AI Dashboard")

    window = DashboardWindow()
    window.show()

    return application.exec()


if __name__ == "__main__":
    raise SystemExit(main())
