#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$HOME/agentic-interview-prep"
VENV_DIR="$HOME/.local/share/interview-ai-dashboard/venv"

cd "$REPO_DIR"
export PYTHONPATH="$REPO_DIR/src"

exec "$VENV_DIR/bin/python" -m interview_ai_dashboard
