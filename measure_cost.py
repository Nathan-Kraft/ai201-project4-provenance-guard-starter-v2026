#!/usr/bin/env python3
"""
Measures the real cost of one /submit run on this machine.

    python app.py                 # in one terminal
    python measure_cost.py        # in another

There's no API bill here, the model runs locally, so the real cost is
seconds of compute. This sends the same piece of text to /submit ten
times, reads back the `duration` each run logged to the audit log (the
time spent inside the two signals plus combining and labelling, not
network or Flask overhead), and reports the average.

Each run uses its own creator_id so the unit 8 rate limiter (keyed on
creator_id) doesn't turn a slow run into a 429.
"""

import sys

import config

TEXT = (
    "The lighthouse keeper climbed the spiral stairs before dawn, same as "
    "every morning for the last eleven years, and lit the lamp against a "
    "grey sky that gave no sign of the storm due that night."
)

RUNS = 10


def main():
    try:
        import requests
    except ImportError:
        print("The `requests` package isn't installed.\n"
              "Run: pip install -r requirements.txt", file=sys.stderr)
        sys.exit(1)

    url = f"http://{config.HOST}:{config.PORT}"
    try:
        requests.get(f"{url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {url}.\n"
              f"Start your service first:  python app.py", file=sys.stderr)
        sys.exit(1)

    durations = []
    for i in range(RUNS):
        response = requests.post(f"{url}/submit", json={
            "text": TEXT,
            "creator_id": f"cost-check-{i}",
        }, timeout=60)
        response.raise_for_status()
        content_id = response.json()["content_id"]

        entries = requests.get(f"{url}/log", timeout=10).json()["entries"]
        entry = next(e for e in entries if e.get("content_id") == content_id
                     and e.get("status") == "decided")
        duration = entry["duration"]
        durations.append(duration)
        print(f"run {i + 1:>2}: {duration:.3f}s")

    average = sum(durations) / len(durations)
    print(f"\n{RUNS} runs, average {average:.3f}s "
          f"(min {min(durations):.3f}s, max {max(durations):.3f}s)")
    print("Measured as the `duration` field each /submit call wrote to "
          "logs/audit.jsonl: time spent inside detector.model_signal, "
          "stylometry.style_signal, and scoring, on this machine, not a "
          "number from any pricing page.")


if __name__ == "__main__":
    main()
