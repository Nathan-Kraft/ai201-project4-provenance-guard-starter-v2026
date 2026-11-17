"""
The audit log.

Every decision your service makes gets written here as one JSON object per
line. Not `print()` — a file you can read back.

The reason is next unit: you run an attack against this service, and **an
attack you can't see in a log is an attack you can't diagnose.** An input that
slipped past your detector leaves no other trace.

All nine fields the unit 8 rubric requires are in the entry shape from the
start, even though unit 7 only fills some of them. That's deliberate — adding
fields later means your early entries and your late ones have different shapes,
and the one you most want to compare is the one from before the change.

    from audit import log_decision, read_entries

    log_decision(content_id=..., creator_id=..., guess="ai", ...)
    entries = read_entries(limit=50)
"""

import json
import threading
from datetime import datetime, timezone

import config

_lock = threading.Lock()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def log_decision(
    content_id: str,
    creator_id: str,
    guess: str | None = None,
    model_score: float | None = None,
    style_score: float | None = None,
    combined_score: float | None = None,
    label: str | None = None,
    status: str = "decided",
    **extra,
) -> dict:
    """
    Write one decision to the audit log.

    The nine required fields, all present from unit 7 whether or not you can
    fill them yet:

        timestamp, content_id, creator_id, guess,
        model_score, style_score, combined_score, label, status

    `status` moves over an item's life: `decided` when first judged,
    `under_review` once the writer appeals.

    Anything extra you pass gets written too — useful for `rejected` entries in
    unit 8, where there's no decision but you still want the trace.
    """
    entry = {
        "timestamp": _now(),
        "content_id": content_id,
        "creator_id": creator_id,
        "guess": guess,
        "model_score": model_score,
        "style_score": style_score,
        "combined_score": combined_score,
        "label": label,
        "status": status,
    }
    entry.update(extra)
    return _append(entry)


def log_appeal(content_id: str, creator_id: str, reasoning: str) -> dict:
    """
    Record an appeal beside the original decision.

    This doesn't overwrite anything. The log is append-only, so the original
    decision stays exactly where it was and the appeal sits after it — which is
    the whole point of an audit log. Someone reading it later can see what was
    decided, that it was challenged, and in what order.
    """
    return _append({
        "timestamp": _now(),
        "content_id": content_id,
        "creator_id": creator_id,
        "event": "appeal",
        "status": "under_review",
        "reasoning": reasoning,
    })


def log_rejection(creator_id: str, reason: str, **extra) -> dict:
    """
    Record a request that never became a decision — a rate-limit rejection or
    an input your route refused.

    ⚠️ Unit 8 asks for this explicitly, and the reason is worth holding onto:
    **an attack that shows up only as an absence is one you'll never find.** A
    thousand requests that got a 429 and left no trace look exactly like a
    quiet afternoon.
    """
    return _append({
        "timestamp": _now(),
        "content_id": None,
        "creator_id": creator_id,
        "guess": None,
        "model_score": None,
        "style_score": None,
        "combined_score": None,
        "label": None,
        "status": "rejected",
        "event": "rejected",
        "reason": reason,
        **extra,
    })


def _append(entry: dict) -> dict:
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    line = json.dumps(entry, ensure_ascii=False)
    with _lock:
        with config.AUDIT_LOG.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    return entry


def read_entries(limit: int | None = None) -> list[dict]:
    """
    Read the log back, oldest first. `limit` keeps the most recent N.

    A malformed line is skipped rather than raising — a log that can't be read
    because of one bad row is worse than a log with a gap.
    """
    if not config.AUDIT_LOG.exists():
        return []

    entries = []
    for line in config.AUDIT_LOG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    return entries[-limit:] if limit else entries


def clear() -> int:
    """Wipe the log. Handy between attack runs; returns how many went."""
    count = len(read_entries())
    if config.AUDIT_LOG.exists():
        config.AUDIT_LOG.unlink()
    return count


def entries_for(content_id: str) -> list[dict]:
    """Every entry touching one content id, in order."""
    return [e for e in read_entries() if e.get("content_id") == content_id]


def latest_decision(entries: list[dict]) -> dict | None:
    """
    Pick the entry that currently holds this content's guess/label/scores.

    `entries_for` returns everything touching a content_id in order: the
    original decision, then any appeal, then any review. Appeals and
    rejections don't carry real guess/label/score values (an appeal entry
    only has `reasoning`, a rejection entry zeroes everything out), so this
    skips those event types and returns the last entry that does carry
    them. A `review` entry counts as a decision here: by the time
    `log_review` writes one, it has already been given a complete
    guess/label pair (unchanged for an upheld appeal, corrected for an
    overturned one), so it's exactly as valid a "current decision" as the
    original one from `/submit`.

    Returns None only if `entries` is empty or contains nothing but
    appeal/rejected events, which shouldn't happen for a real content_id
    (every content_id starts with a `log_decision` call).
    """
    decisions = [e for e in entries if e.get("event") not in ("appeal", "rejected")]
    return decisions[-1] if decisions else None


def current_status(content_id: str) -> dict | None:
    """
    Where one piece of content stands right now, derived from the log.

    There's no separate "state" anywhere — the log is append-only, so
    "current" always means "work it out from the entries so far." `status`
    comes from the very last entry for this id, whatever kind it is,
    because status is the one field every event type sets correctly
    (`decided`, `under_review`, `resolved`, `rejected`). The guess/label/
    scores instead come from `latest_decision`, since an appeal entry
    itself carries no such values — it only records that one was
    challenged, not a new one.

    Returns None if content_id has no entries at all, which both
    `GET /content/<id>` and `GET /queue` treat as "nothing by that id was
    ever submitted."
    """
    entries = entries_for(content_id)
    if not entries:
        return None
    decision = latest_decision(entries)
    return {
        "content_id": content_id,
        "status": entries[-1].get("status"),
        "guess": decision.get("guess") if decision else None,
        "label": decision.get("label") if decision else None,
        "model_score": decision.get("model_score") if decision else None,
        "style_score": decision.get("style_score") if decision else None,
        "combined_score": decision.get("combined_score") if decision else None,
        "creator_id": decision.get("creator_id") if decision else entries[0].get("creator_id"),
    }


def log_review(content_id: str, reviewer_id: str, decision: str,
                guess: str | None, label: str | None, notes: str = "") -> dict:
    """
    Record a human reviewer's resolution of an appeal.

    Like `log_appeal`, this only appends — the original decision entry (and
    the appeal entry) are never touched, so the full history of what the
    detector first said, that it was challenged, and what a person decided
    about it stays intact and in order.

    `decision` is "uphold" or "overturn" (the route validates this before
    calling in — this function just records whatever it's given). The
    caller is also responsible for working out `guess`/`label`: for an
    upheld appeal they're the content's existing values carried forward
    unchanged; for an overturned one they're the reviewer's correction. That
    choice happens in `app.py` rather than here because it depends on
    `scoring.label_for_guess`, which this module has no reason to know
    about.

    Sets status "resolved", which is what takes an item out of
    `GET /queue` — `current_status` will report this entry's guess/label
    as the content's current ones from this point on.
    """
    return _append({
        "timestamp": _now(),
        "content_id": content_id,
        "creator_id": None,
        "reviewer_id": reviewer_id,
        "guess": guess,
        "label": label,
        "event": "review",
        "status": "resolved",
        "decision": decision,
        "notes": notes,
    })

