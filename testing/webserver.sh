#!/usr/bin/sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 -m http.server -d "${SCRIPT_DIR}" 8743
