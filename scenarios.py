"""
What your test runs. <- UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.

Criterion 3 (the appeal path) isn't here. It needs a submission's content_id
fed into a second call to /appeal, which this file's two shapes can't express.
Tested by hand instead, written up as such.
"""

import json
from pathlib import Path

SAMPLES = Path(__file__).parent / "samples"


def _text(filename):
    return json.loads((SAMPLES / filename).read_text(encoding="utf-8"))["text"]


HUMAN_10 = [
    "clearly_human.json", "clearly_human_02.json", "clearly_human_03.json",
    "clearly_human_04.json", "clearly_human_05.json", "clearly_human_06.json",
    "clearly_human_07.json", "clearly_human_08.json", "clearly_human_09.json",
    "formal_human.json",
]

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # Confirmed human writing, 10 pieces across different registers.
        # See samples/README.md for what each one is.
        "texts": [_text(f) for f in HUMAN_10],
    },
    {
        "name": "bad input",
        "criterion": 2,
        # Missing text, empty text, whitespace-only text, and text over
        # 50,000 characters — 5 tries each, since this must be deterministic.
        "bodies": (
            [{"creator_id": f"eval_bad_missing_{i}"} for i in range(1, 6)]
            + [{"text": "", "creator_id": f"eval_bad_empty_{i}"} for i in range(1, 6)]
            + [{"text": "   ", "creator_id": f"eval_bad_ws_{i}"} for i in range(1, 6)]
            + [{"text": "word " * 50000, "creator_id": f"eval_bad_huge_{i}"} for i in range(1, 6)]
        ),
    },
    {
        "name": "label coverage",
        "criterion": 4,
        # A mix of 3 clearly-human, 3 clearly-AI, and 4 borderline texts, so
        # all three `guess` values should show up somewhere in this set.
        "texts": [
            _text("clearly_human_02.json"),
            _text("clearly_human_05.json"),
            _text("clearly_human_08.json"),
            _text("clearly_ai_02.json"),
            _text("clearly_ai_03.json"),
            _text("clearly_ai_04.json"),
            _text("borderline.json"),
            _text("borderline_02.json"),
            _text("borderline_03.json"),
            _text("borderline_04.json"),
        ],
    },
    {
        "name": "correct side",
        "criterion": 5,
        # 5 clearly-human, 5 clearly-AI. Ground truth isn't stored here,
        # checked against samples/README.md when scoring the run.
        "texts": [
            _text("clearly_human.json"),
            _text("clearly_human_03.json"),
            _text("clearly_human_06.json"),
            _text("clearly_human_07.json"),
            _text("clearly_human_09.json"),
            _text("clearly_ai.json"),
            _text("clearly_ai_02.json"),
            _text("clearly_ai_03.json"),
            _text("clearly_ai_04.json"),
            _text("clearly_ai_05.json"),
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
