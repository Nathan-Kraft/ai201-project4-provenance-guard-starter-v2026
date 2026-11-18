#!/usr/bin/env python3
"""
A terminal tool for working the review queue, instead of hand-building curl
commands for every resolution.

    python app.py                 # in one terminal
    python review_cli.py          # in another

Asks for a reviewer_id once at the start and reuses it for every resolution
in the run. Re-fetches /queue after each resolve rather than working off a
list fetched once, so an item someone else resolves mid-session doesn't get
acted on twice.
"""

import sys

import config

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"


def require_requests():
    try:
        import requests  # noqa: F401
    except ImportError:
        print("The `requests` package isn't installed.\n"
              "Run: pip install -r requirements.txt", file=sys.stderr)
        sys.exit(1)


def prompt_action():
    while True:
        choice = input("  [u]phold / [o]verturn / [s]kip / [q]uit: ").strip().lower()
        if choice in ("u", "o", "s", "q", ""):
            return choice or "s"
        print("  Not a valid choice.")


def prompt_corrected_guess():
    while True:
        guess = input("  corrected_guess (ai/human/unsure): ").strip().lower()
        if guess in ("ai", "human", "unsure"):
            return guess
        print("  Has to be one of: ai, human, unsure.")


def main():
    require_requests()
    import requests

    url = DEFAULT_URL
    try:
        requests.get(f"{url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {url}.\n"
              f"Start your service first:  python app.py", file=sys.stderr)
        sys.exit(1)

    reviewer_id = input("Reviewer id: ").strip() or "unknown"

    while True:
        queue = requests.get(f"{url}/queue", timeout=10).json()["queue"]
        if not queue:
            print("\nQueue is empty.")
            return

        item = queue[0]
        content = requests.get(f"{url}/content/{item['content_id']}", timeout=10).json()

        print(f"\ncontent_id: {item['content_id']}")
        print(f"creator_id: {content.get('creator_id')}")
        print(f"guess:      {content.get('guess')}  ({content.get('label')})")
        print(f"scores:     model={content.get('model_score')} "
              f"style={content.get('style_score')} "
              f"combined={content.get('combined_score')}")
        print(f"reasoning:  {item['reasoning']}")
        print(f"queued since: {item['queued_since']}")
        print("\n--- submitted text ---")
        print(content.get("text") or "(not available)")
        print("---")

        action = prompt_action()
        if action == "q":
            return
        if action == "s":
            print("Skipped.")
            continue

        decision = "uphold" if action == "u" else "overturn"
        body = {"decision": decision, "reviewer_id": reviewer_id}
        if decision == "overturn":
            body["corrected_guess"] = prompt_corrected_guess()
        notes = input("  notes (optional): ").strip()
        if notes:
            body["notes"] = notes

        response = requests.post(f"{url}/resolve/{item['content_id']}",
                                 json=body, timeout=30)
        print(f"  -> {response.status_code} {response.json()}")


if __name__ == "__main__":
    main()
