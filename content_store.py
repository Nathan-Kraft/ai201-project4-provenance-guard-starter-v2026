"""
Raw submitted text, stored separately from the audit log.

audit.py's log is meant to be exported and pasted around freely (`GET /log`,
results written into the README) and, in this project, `logs/audit.jsonl` is
tracked in git. Raw submission text doesn't belong in something handed out
and committed that casually, so it gets its own file instead, and that file
is gitignored.

One record per content_id, append-only like audit.py for the same reason:
never touch what's already on disk, just add to it.
"""

import json
import threading

import config

_lock = threading.Lock()


def save(content_id: str, text: str) -> None:
    config.CONTENT_STORE.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps({"content_id": content_id, "text": text}, ensure_ascii=False)
    with _lock:
        with config.CONTENT_STORE.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


def get(content_id: str) -> str | None:
    """The text for one content_id, or None if there isn't one on file."""
    if not config.CONTENT_STORE.exists():
        return None

    match = None
    for line in config.CONTENT_STORE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if record.get("content_id") == content_id:
            match = record.get("text")

    return match
