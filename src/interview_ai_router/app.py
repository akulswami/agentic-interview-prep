from __future__ import annotations

import json
import os
import re
import time
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, AsyncIterator

import httpx
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse

app = FastAPI(title="Interview Prep Auto Router")

LITELLM_BASE_URL = os.environ.get(
    "LITELLM_BASE_URL",
    "http://127.0.0.1:4000/v1",
).rstrip("/")
LITELLM_MASTER_KEY = os.environ["LITELLM_MASTER_KEY"]
EXPECTED_ROUTER_KEY = os.environ["AUTO_ROUTER_KEY"]

LOG_PATH = Path(
    os.environ.get(
        "AUTO_ROUTER_LOG",
        str(Path.home() / ".local/state/interview-prep-router/usage.jsonl"),
    )
)

LIVE_PATH = Path(
    os.environ.get(
        "AUTO_ROUTER_LIVE",
        str(Path.home() / ".local/state/interview-prep-router/live.json"),
    )
)

LOCAL_MODEL = "interview-local"
CLAUDE_MODEL = "interview-claude"

CLAUDE_INPUT_USD_PER_MTOK = float(
    os.environ.get("CLAUDE_INPUT_USD_PER_MTOK", "3")
)
CLAUDE_OUTPUT_USD_PER_MTOK = float(
    os.environ.get("CLAUDE_OUTPUT_USD_PER_MTOK", "15")
)

CLAUDE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    (
        "explicit_cloud_request",
        re.compile(r"\b(use|route to|ask)\s+claude\b|^/claude\b", re.I),
    ),
    (
        "high_stakes_domain",
        re.compile(
            r"\b(legal|immigration|petition|visa|medical advice|diagnosis|"
            r"clinical|publication-quality|peer review)\b",
            re.I,
        ),
    ),
    (
        "concurrency_or_security",
        re.compile(
            r"\b(race condition|deadlock|lock ordering|memory model|"
            r"atomic ordering|cryptograph|security audit|vulnerability|"
            r"threat model)\b",
            re.I,
        ),
    ),
    (
        "architecture",
        re.compile(
            r"\b(system design|architecture decision|architectural trade-?off|"
            r"distributed system|fault tolerance|scalability)\b",
            re.I,
        ),
    ),
    (
        "complex_debugging",
        re.compile(
            r"\b(root cause|complex debugging|intermittent crash|"
            r"heisenbug|multi-threaded bug|cross-file bug)\b",
            re.I,
        ),
    ),
    (
        "multi_file_change",
        re.compile(
            r"\b(multi-file|multiple files|repository-wide|repo-wide|"
            r"large refactor|cross-cutting refactor)\b",
            re.I,
        ),
    ),
]

LOCAL_FORCE_PATTERN = re.compile(r"^/local\b", re.I)
CLAUDE_FORCE_PATTERN = re.compile(r"^/claude\b", re.I)

CONTINUATION_PATTERN = re.compile(
    r"(?im)^\s*"
    r"(?:"
    r"continue(?:\s+(?:your|the|this))?\s+(?:response|answer)"
    r"(?:\s+(?:exactly\s+)?where\s+you\s+left\s+off)?"
    r"|continue\s+(?:exactly\s+)?where\s+you\s+left\s+off"
    r"|go\s+on"
    r"|finish\s+(?:the|your)\s+(?:response|answer)"
    r")"
    r"\s*[:.!]?\s*$"
)

CONTINUATION_WINDOW = timedelta(minutes=5)


def authorize(authorization: str | None) -> None:
    if authorization != f"Bearer {EXPECTED_ROUTER_KEY}":
        raise HTTPException(status_code=401, detail="Invalid router key")


def flatten_text(value: Any) -> str:
    if isinstance(value, str):
        return value

    if isinstance(value, list):
        return "\n".join(
            item.get("text", "")
            for item in value
            if isinstance(item, dict) and isinstance(item.get("text"), str)
        )

    return ""


def normalize_text(value: str) -> str:
    return " ".join(value.split())


def task_label(messages: list[dict[str, Any]]) -> str:
    text = latest_user_prompt(messages)
    text = re.sub(
        r"^\s*/(?:local|claude)\b\s*",
        "",
        text,
        count=1,
        flags=re.I,
    )

    continuation_match = CONTINUATION_PATTERN.search(text)

    if continuation_match:
        return normalize_text(continuation_match.group(0))[:160]

    lines = [
        normalize_text(line)
        for line in text.splitlines()
        if normalize_text(line)
    ]

    for line in reversed(lines):
        if len(line) <= 240:
            return line[:160]

    return normalize_text(text)[:160] or "Untitled request"


def latest_successful_route() -> str | None:
    if not LOG_PATH.exists():
        return None

    cutoff = datetime.now(timezone.utc) - CONTINUATION_WINDOW

    try:
        lines = LOG_PATH.read_text(
            encoding="utf-8",
        ).splitlines()
    except OSError:
        return None

    for line in reversed(lines):
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue

        if record.get("record_type") == "feedback":
            continue

        if record.get("success") is not True:
            continue

        route = record.get("route")

        if route not in {LOCAL_MODEL, CLAUDE_MODEL}:
            continue

        timestamp_text = record.get("timestamp")

        if not isinstance(timestamp_text, str):
            continue

        try:
            timestamp = datetime.fromisoformat(timestamp_text)
        except ValueError:
            continue

        if timestamp.tzinfo is None:
            timestamp = timestamp.replace(tzinfo=timezone.utc)

        if timestamp < cutoff:
            return None

        return str(route)

    return None


def combined_prompt(messages: list[dict[str, Any]]) -> str:
    return "\n".join(
        flatten_text(message.get("content", ""))
        for message in messages
    )


def latest_user_prompt(messages: list[dict[str, Any]]) -> str:
    for message in reversed(messages):
        if message.get("role") == "user":
            return flatten_text(message.get("content", "")).strip()
    return ""


def classify(messages: list[dict[str, Any]]) -> tuple[str, str]:
    latest_text = latest_user_prompt(messages)
    full_text = combined_prompt(messages)

    if LOCAL_FORCE_PATTERN.search(latest_text):
        return LOCAL_MODEL, "forced_local"

    if CLAUDE_FORCE_PATTERN.search(latest_text):
        return CLAUDE_MODEL, "forced_claude"

    if CONTINUATION_PATTERN.search(latest_text):
        previous_route = latest_successful_route()

        if previous_route == LOCAL_MODEL:
            return LOCAL_MODEL, "continuation_previous_local"

        if previous_route == CLAUDE_MODEL:
            return CLAUDE_MODEL, "continuation_previous_claude"

    # Classify task intent from the latest user request, not historical chat.
    for reason, pattern in CLAUDE_PATTERNS:
        if pattern.search(latest_text):
            return CLAUDE_MODEL, reason

    # Context-size routing still considers the complete payload.
    if len(full_text) > 24_000:
        return CLAUDE_MODEL, "large_prompt"

    return LOCAL_MODEL, "default_local"


def strip_route_prefix(messages: list[dict[str, Any]]) -> None:
    for message in reversed(messages):
        content = message.get("content")
        if isinstance(content, str):
            message["content"] = re.sub(
                r"^\s*/(?:local|claude)\b\s*",
                "",
                content,
                count=1,
                flags=re.I,
            )
            return


def sonnet_equivalent_cost(
    prompt_tokens: int,
    completion_tokens: int,
) -> float:
    return (
        prompt_tokens * CLAUDE_INPUT_USD_PER_MTOK
        + completion_tokens * CLAUDE_OUTPUT_USD_PER_MTOK
    ) / 1_000_000


def append_log(record: dict[str, Any]) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_live_snapshot(record: dict[str, Any]) -> None:
    LIVE_PATH.parent.mkdir(parents=True, exist_ok=True)

    temporary_path = LIVE_PATH.with_suffix(".json.tmp")
    temporary_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary_path.replace(LIVE_PATH)


def live_record(
    *,
    request_id: str,
    status: str,
    selected_model: str,
    reason: str,
    task: str,
    started_at: str,
    started_monotonic: float,
    streamed_characters: int = 0,
    estimated_completion_tokens: int = 0,
    prompt_tokens: int = 0,
    completion_tokens: int = 0,
    error: str | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "request_id": request_id,
        "status": status,
        "route": selected_model,
        "reason": reason,
        "task_label": task,
        "started_at": started_at,
        "elapsed_seconds": round(
            time.perf_counter() - started_monotonic,
            3,
        ),
        "streamed_characters": streamed_characters,
        "estimated_completion_tokens": estimated_completion_tokens,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
    }

    if error:
        record["error"] = error

    return record


@app.get("/health")
async def health(
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    authorize(authorization)
    return {
        "status": "ok",
        "service": "interview-ai-router",
        "source": "repository",
        "litellm": LITELLM_BASE_URL,
        "local_model": LOCAL_MODEL,
        "claude_model": CLAUDE_MODEL,
    }


@app.get("/v1/models")
async def models(
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    authorize(authorization)
    return {
        "object": "list",
        "data": [
            {
                "id": "interview-auto",
                "object": "model",
                "created": 0,
                "owned_by": "interview-prep-router",
            }
        ],
    }


@app.post("/v1/chat/completions", response_model=None)
async def chat_completions(
    request: Request,
    authorization: str | None = Header(default=None),
):
    authorize(authorization)

    request_id = str(uuid.uuid4())
    started = time.perf_counter()
    started_at = datetime.now(timezone.utc).isoformat()
    body = await request.json()

    messages = body.get("messages")
    if not isinstance(messages, list):
        raise HTTPException(status_code=400, detail="messages must be a list")

    selected_model, reason = classify(messages)
    label = task_label(messages)
    strip_route_prefix(messages)

    write_live_snapshot(
        live_record(
            request_id=request_id,
            status="routing",
            selected_model=selected_model,
            reason=reason,
            task=label,
            started_at=started_at,
            started_monotonic=started,
        )
    )

    upstream_body = dict(body)
    upstream_body["model"] = selected_model

    requested_stream = bool(body.get("stream", False))

    headers = {
        "Authorization": f"Bearer {LITELLM_MASTER_KEY}",
        "Content-Type": "application/json",
    }

    if requested_stream:
        client = httpx.AsyncClient(timeout=300.0)
        upstream_request = client.build_request(
            "POST",
            f"{LITELLM_BASE_URL}/chat/completions",
            headers=headers,
            json=upstream_body,
        )
        upstream = await client.send(upstream_request, stream=True)

        write_live_snapshot(
            live_record(
                request_id=request_id,
                status="generating",
                selected_model=selected_model,
                reason=reason,
                task=label,
                started_at=started_at,
                started_monotonic=started,
            )
        )

        if upstream.status_code >= 400:
            content = await upstream.aread()
            await upstream.aclose()
            await client.aclose()
            return JSONResponse(
                status_code=upstream.status_code,
                content=json.loads(content),
            )

        async def relay_stream() -> AsyncIterator[bytes]:
            prompt_tokens = 0
            completion_tokens = 0
            streamed_characters = 0
            estimated_completion_tokens = 0

            try:
                async for chunk in upstream.aiter_bytes():
                    yield chunk

                    decoded_chunk = chunk.decode(
                        "utf-8",
                        errors="ignore",
                    )

                    for line in decoded_chunk.splitlines():
                        if not line.startswith("data: "):
                            continue

                        payload = line[6:].strip()
                        if payload == "[DONE]":
                            continue

                        try:
                            event = json.loads(payload)
                        except json.JSONDecodeError:
                            continue

                        choices = event.get("choices") or []

                        for choice in choices:
                            delta = choice.get("delta") or {}
                            content = delta.get("content")

                            if isinstance(content, str):
                                streamed_characters += len(content)

                        estimated_completion_tokens = max(
                            estimated_completion_tokens,
                            round(streamed_characters / 4),
                        )

                        usage = event.get("usage") or {}
                        prompt_tokens = int(
                            usage.get("prompt_tokens") or prompt_tokens
                        )
                        completion_tokens = int(
                            usage.get("completion_tokens")
                            or completion_tokens
                        )

                        write_live_snapshot(
                            live_record(
                                request_id=request_id,
                                status="generating",
                                selected_model=selected_model,
                                reason=reason,
                                task=label,
                                started_at=started_at,
                                started_monotonic=started,
                                streamed_characters=streamed_characters,
                                estimated_completion_tokens=(
                                    estimated_completion_tokens
                                ),
                                prompt_tokens=prompt_tokens,
                                completion_tokens=completion_tokens,
                            )
                        )
            finally:
                await upstream.aclose()
                await client.aclose()

                equivalent_cost = sonnet_equivalent_cost(
                    prompt_tokens,
                    completion_tokens,
                )

                write_live_snapshot(
                    live_record(
                        request_id=request_id,
                        status="completed",
                        selected_model=selected_model,
                        reason=reason,
                        task=label,
                        started_at=started_at,
                        started_monotonic=started,
                        streamed_characters=streamed_characters,
                        estimated_completion_tokens=(
                            estimated_completion_tokens
                        ),
                        prompt_tokens=prompt_tokens,
                        completion_tokens=completion_tokens,
                    )
                )

                append_log(
                    {
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "request_id": request_id,
                        "requested_model": body.get("model"),
                        "route": selected_model,
                        "reason": reason,
                        "task_label": label,
                        "success": True,
                        "stream": True,
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": completion_tokens,
                        "total_tokens": prompt_tokens + completion_tokens,
                        "latency_seconds": round(
                            time.perf_counter() - started,
                            3,
                        ),
                        "actual_claude_cost_usd_estimate": round(
                            equivalent_cost
                            if selected_model == CLAUDE_MODEL
                            else 0.0,
                            8,
                        ),
                        "avoided_claude_cost_usd_estimate": round(
                            equivalent_cost
                            if selected_model == LOCAL_MODEL
                            else 0.0,
                            8,
                        ),
                    }
                )

        return StreamingResponse(
            relay_stream(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "X-Accel-Buffering": "no",
                "X-Interview-Route": selected_model,
                "X-Interview-Reason": reason,
                "X-Interview-Request-Id": request_id,
            },
        )

    write_live_snapshot(
        live_record(
            request_id=request_id,
            status="generating",
            selected_model=selected_model,
            reason=reason,
            task=label,
            started_at=started_at,
            started_monotonic=started,
        )
    )

    async with httpx.AsyncClient(timeout=300.0) as client:
        upstream = await client.post(
            f"{LITELLM_BASE_URL}/chat/completions",
            headers=headers,
            json=upstream_body,
        )

    try:
        response_body = upstream.json()
    except ValueError as exc:
        raise HTTPException(
            status_code=502,
            detail="Upstream returned invalid JSON",
        ) from exc

    if upstream.status_code >= 400:
        return JSONResponse(
            status_code=upstream.status_code,
            content=response_body,
        )

    usage = response_body.get("usage") or {}
    prompt_tokens = int(usage.get("prompt_tokens") or 0)
    completion_tokens = int(usage.get("completion_tokens") or 0)

    equivalent_cost = sonnet_equivalent_cost(
        prompt_tokens,
        completion_tokens,
    )

    write_live_snapshot(
        live_record(
            request_id=request_id,
            status="completed",
            selected_model=selected_model,
            reason=reason,
            task=label,
            started_at=started_at,
            started_monotonic=started,
            estimated_completion_tokens=completion_tokens,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
        )
    )

    append_log(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "request_id": request_id,
            "requested_model": body.get("model"),
            "route": selected_model,
            "reason": reason,
            "task_label": label,
            "success": True,
            "stream": False,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
            "latency_seconds": round(time.perf_counter() - started, 3),
            "actual_claude_cost_usd_estimate": round(
                equivalent_cost if selected_model == CLAUDE_MODEL else 0.0,
                8,
            ),
            "avoided_claude_cost_usd_estimate": round(
                equivalent_cost if selected_model == LOCAL_MODEL else 0.0,
                8,
            ),
        }
    )

    response_body["model"] = selected_model
    response_body["router"] = {
        "reason": reason,
        "request_id": request_id,
    }

    return JSONResponse(content=response_body)
