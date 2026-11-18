#!/usr/bin/env python3
"""
Run the five capstone criteria three times each.

    python app.py
    python run_capstone_eval.py --label after

Unlike run_eval.py, these scenarios use several requests per trial. They
submit content, file appeals, inspect the queue, and resolve or reject review
requests. Each scenario uses unique creator and content ids so old log entries
do not affect its checks.
"""

import argparse
import datetime as dt
import json
import sys
import time

import config


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass


DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"
TEXT = "This is a capstone evaluator submission with enough words for scoring."


def request_json(requests, method, url, path, body=None, timeout=90.0):
    """Send one request and return its status, JSON body, or an error."""
    try:
        response = requests.request(
            method,
            f"{url}{path}",
            json=body,
            timeout=timeout,
        )
        try:
            payload = response.json()
        except ValueError:
            payload = {}
        return {
            "status": response.status_code,
            "body": payload,
        }
    except Exception as exc:
        return {
            "status": None,
            "body": {},
            "error": f"{type(exc).__name__}: {exc}",
        }


def submit(requests, url, suffix, timeout):
    """Submit one unique item and return the request result."""
    return request_json(
        requests,
        "POST",
        url,
        "/submit",
        {
            "text": TEXT,
            "creator_id": f"capstone_{suffix}",
        },
        timeout,
    )


def content_id_from(result):
    """Get a content id without raising if a setup request failed."""
    return result.get("body", {}).get("content_id")


def appeal(requests, url, content_id, suffix, timeout):
    return request_json(
        requests,
        "POST",
        url,
        "/appeal",
        {
            "content_id": content_id,
            "reasoning": f"Capstone appeal {suffix}.",
        },
        timeout,
    )


def get_content(requests, url, content_id, timeout):
    return request_json(requests, "GET", url, f"/content/{content_id}", timeout=timeout)


def get_queue(requests, url, timeout):
    return request_json(requests, "GET", url, "/queue", timeout=timeout)


def resolve(requests, url, content_id, body, timeout):
    return request_json(
        requests,
        "POST",
        url,
        f"/resolve/{content_id}",
        body,
        timeout,
    )


def queue_items(queue_result, content_ids):
    """Return queue rows for the ids created by one trial, in response order."""
    rows = queue_result.get("body", {}).get("queue", [])
    return [row for row in rows if row.get("content_id") in content_ids]


def run_queue_membership(requests, url, trial, timeout):
    ids = []
    setup = []
    for kind in ("under_review", "resolved", "resolved", "never_appealed"):
        suffix = f"membership_{trial}_{kind}_{len(ids)}"
        submitted = submit(requests, url, suffix, timeout)
        content_id = content_id_from(submitted)
        setup.append({"submit": submitted})
        if not content_id:
            continue
        ids.append(content_id)
        if kind != "never_appealed":
            appealed = appeal(requests, url, content_id, suffix, timeout)
            setup[-1]["appeal"] = appealed
        if kind == "resolved":
            setup[-1]["resolve"] = resolve(
                requests,
                url,
                content_id,
                {
                    "decision": "uphold",
                    "reviewer_id": f"capstone_reviewer_{trial}",
                },
                timeout,
            )

    queued = ids[0] if ids else None
    queue_result = get_queue(requests, url, timeout)
    observed = [row.get("content_id") for row in queue_items(queue_result, ids)]
    return {
        "created_content_ids": ids,
        "expected_under_review": [queued] if queued else [],
        "queue": queue_result,
        "observed_created_ids": observed,
        "passed": (
            queue_result.get("status") == 200
            and observed == ([queued] if queued else [])
        ),
        "setup": setup,
    }


def run_queue_order(requests, url, trial, timeout, pause):
    ids = []
    setup = []
    for index in range(3):
        suffix = f"ordering_{trial}_{index}"
        submitted = submit(requests, url, suffix, timeout)
        content_id = content_id_from(submitted)
        entry = {"submit": submitted}
        if content_id:
            ids.append(content_id)
            entry["appeal"] = appeal(requests, url, content_id, suffix, timeout)
        setup.append(entry)
        if index < 2:
            time.sleep(pause)

    queue_result = get_queue(requests, url, timeout)
    observed = [
        row.get("content_id")
        for row in queue_items(queue_result, ids)
    ]
    return {
        "expected_order": ids,
        "queue": queue_result,
        "observed_order": observed,
        "passed": queue_result.get("status") == 200 and observed == ids,
        "setup": setup,
    }


def run_overturn(requests, url, trial, timeout):
    checks = []
    corrected_guesses = ("ai", "human", "unsure", "ai", "human")
    for index, corrected_guess in enumerate(corrected_guesses):
        suffix = f"overturn_{trial}_{index}"
        submitted = submit(requests, url, suffix, timeout)
        content_id = content_id_from(submitted)
        entry = {"submit": submitted, "corrected_guess": corrected_guess}
        if content_id:
            entry["appeal"] = appeal(requests, url, content_id, suffix, timeout)
            entry["resolve"] = resolve(
                requests,
                url,
                content_id,
                {
                    "decision": "overturn",
                    "corrected_guess": corrected_guess,
                    "reviewer_id": f"capstone_reviewer_{trial}",
                },
                timeout,
            )
            entry["content"] = get_content(requests, url, content_id, timeout)
            resolved = entry["resolve"].get("body", {})
            current = entry["content"].get("body", {})
            entry["matches"] = (
                resolved.get("guess") == corrected_guess
                and current.get("guess") == corrected_guess
                and current.get("label") == resolved.get("label")
            )
        else:
            entry["matches"] = False
        checks.append(entry)

    return {
        "checks": checks,
        "passed": all(entry["matches"] for entry in checks),
    }


def run_invalid_corrected_guess(requests, url, trial, timeout):
    suffix = f"invalid_guess_{trial}"
    submitted = submit(requests, url, suffix, timeout)
    content_id = content_id_from(submitted)
    entry = {"submit": submitted, "corrected_guess": "banana"}
    if not content_id:
        entry["passed"] = False
        return entry

    entry["appeal"] = appeal(requests, url, content_id, suffix, timeout)
    entry["before"] = get_content(requests, url, content_id, timeout)
    entry["resolve"] = resolve(
        requests,
        url,
        content_id,
        {
            "decision": "overturn",
            "corrected_guess": "banana",
            "reviewer_id": f"capstone_reviewer_{trial}",
        },
        timeout,
    )
    entry["after"] = get_content(requests, url, content_id, timeout)
    entry["queue"] = get_queue(requests, url, timeout)
    after_body = entry["after"].get("body", {})
    queued_ids = [
        row.get("content_id")
        for row in queue_items(entry["queue"], [content_id])
    ]
    entry["passed"] = (
        entry["resolve"].get("status") == 400
        and after_body.get("status") == "under_review"
        and queued_ids == [content_id]
    )
    return entry


def run_rejected_resolve(requests, url, trial, timeout):
    suffix = f"rejected_resolve_{trial}"
    submitted = submit(requests, url, suffix, timeout)
    content_id = content_id_from(submitted)
    entry = {"submit": submitted}
    if not content_id:
        entry["passed"] = False
        return entry

    entry["appeal"] = appeal(requests, url, content_id, suffix, timeout)
    entry["before"] = get_content(requests, url, content_id, timeout)
    entry["resolve"] = resolve(
        requests,
        url,
        content_id,
        {
            "decision": "maybe",
            "reviewer_id": f"capstone_reviewer_{trial}",
        },
        timeout,
    )
    entry["after"] = get_content(requests, url, content_id, timeout)
    entry["queue"] = get_queue(requests, url, timeout)
    after_body = entry["after"].get("body", {})
    queued_ids = [
        row.get("content_id")
        for row in queue_items(entry["queue"], [content_id])
    ]
    entry["passed"] = (
        entry["resolve"].get("status") == 400
        and after_body.get("status") == "under_review"
        and queued_ids == [content_id]
    )
    return entry


SCENARIOS = (
    ("queue membership", run_queue_membership),
    ("queue ordering", run_queue_order),
    ("overturn replaces state", run_overturn),
    ("invalid corrected_guess", run_invalid_corrected_guess),
    ("rejected resolve preserves status", run_rejected_resolve),
)


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=90.0)
    parser.add_argument(
        "--ordering-pause",
        type=float,
        default=1.1,
        help="Seconds between ordering appeals so timestamps are distinct.",
    )
    args = parser.parse_args()

    try:
        import requests
    except ImportError:
        print(
            "The `requests` package isn't installed.\n"
            "Run: pip install -r requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        health = requests.get(f"{args.url}/health", timeout=5)
        if health.status_code != 200:
            raise RuntimeError(f"health returned HTTP {health.status_code}")
    except Exception as exc:
        print(
            f"Nothing answering at {args.url}: {exc}\n"
            "Start it with: python app.py",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.trials < 3:
        print(f"Warning: {args.trials} trial(s). The submission asks for three.")

    rows = []
    for name, runner in SCENARIOS:
        print(f"\n{name}")
        trials = []
        for trial in range(1, args.trials + 1):
            if name == "queue ordering":
                result = runner(
                    requests,
                    args.url,
                    trial,
                    args.timeout,
                    args.ordering_pause,
                )
            else:
                result = runner(requests, args.url, trial, args.timeout)
            trials.append(result)
            print(f"  trial {trial}: {'PASS' if result.get('passed') else 'CHECK'}")
        rows.append({"name": name, "trials": trials})

    write_report(rows, args)


def write_report(rows, args):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"capstone_run_{stamp}{label}.md"

    n = args.trials
    headers = " | ".join(f"Run {i}" for i in range(1, n + 1))
    divider = "|".join(["---"] * n)
    lines = [
        f"# Capstone run{f' - {args.label}' if args.label else ''}",
        "",
        f"- {n} trials per criterion",
        f"- {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"| Criterion | Target | {headers} | Verdict |",
        f"|---|---|{divider}|---|",
    ]

    for row in rows:
        verdicts = [
            "PASS" if trial.get("passed") else "CHECK"
            for trial in row["trials"]
        ]
        lines.append(
            f"| {row['name']} |  | {' | '.join(verdicts)} |  |"
        )

    lines += [
        "",
        "---",
        "",
        "## What actually came back",
        "",
        "The JSON below records the requests, responses, and checks for each trial.",
        "",
    ]
    for row in rows:
        lines += [f"### {row['name']}", ""]
        for trial_number, result in enumerate(row["trials"], 1):
            lines += [
                f"**Trial {trial_number}**",
                "",
                "```json",
                json.dumps(result, indent=2),
                "```",
                "",
            ]

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")
    print("Fill in the Target and Verdict columns from criteria.md.")


if __name__ == "__main__":
    main()
