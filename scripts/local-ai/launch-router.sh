#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${INTERVIEW_PREP_REPO:-$HOME/agentic-interview-prep}"
ROUTER_VENV="${INTERVIEW_ROUTER_VENV:-$HOME/.local/share/interview-prep-router/venv}"
SECRETS_FILE="${INTERVIEW_ROUTER_SECRETS:-$HOME/.config/interview-prep-router/secrets.env}"
ROUTER_HOST="${INTERVIEW_ROUTER_HOST:-127.0.0.1}"
ROUTER_PORT="${INTERVIEW_ROUTER_PORT:-4100}"

if [[ ! -d "$REPO_DIR" ]]; then
    printf 'Repository not found: %s\n' "$REPO_DIR" >&2
    exit 1
fi

if [[ ! -x "$ROUTER_VENV/bin/python" ]]; then
    printf 'Router virtual environment not found: %s\n' "$ROUTER_VENV" >&2
    exit 1
fi

if [[ ! -f "$SECRETS_FILE" ]]; then
    printf 'Router secrets file not found: %s\n' "$SECRETS_FILE" >&2
    exit 1
fi

cd "$REPO_DIR"

set -a
# shellcheck disable=SC1090
source "$SECRETS_FILE"
set +a

export PYTHONPATH="$REPO_DIR/src${PYTHONPATH:+:$PYTHONPATH}"

exec "$ROUTER_VENV/bin/python" -m uvicorn \
    interview_ai_router.app:app \
    --host "$ROUTER_HOST" \
    --port "$ROUTER_PORT"
