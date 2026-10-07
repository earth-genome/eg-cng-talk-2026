#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

PORT=4200
HOST=127.0.0.1

# Quarto often skips re-render on custom.scss-only saves; touch index.qmd when assets change.
if command -v uv >/dev/null 2>&1; then
  uv run python scripts/watch_assets.py &
elif command -v python3 >/dev/null 2>&1; then
  python3 scripts/watch_assets.py &
else
  echo "Need python3 or uv to watch custom.scss for hot reload." >&2
fi
WATCH_PID=$!
trap 'kill "$WATCH_PID" 2>/dev/null || true' EXIT

echo "Preview: http://${HOST}:${PORT}/"
exec quarto preview index.qmd --port "$PORT" --host "$HOST" --render revealjs "$@"
