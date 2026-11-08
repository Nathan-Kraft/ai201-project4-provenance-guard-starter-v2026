# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

<!-- Your criterion. It must name a number. -->

Given 10 submissions of text confirmed to be human-written, at most 1 may result in a false positive (the response's `guess` field equals `"ai"`).


**Why this target:**

A wrong accusation costs a real person something a missed detection never does: their name attached to a decision they didn't earn. The student we traced writes plainly on purpose, not because they used AI, and could still clear the threshold on both signals at once. Zero tolerance sounds right in principle, but this project's own instructions point out that the first signal runs a model, so identical text can score differently across runs. Demanding 0 of 10 risks failing this criterion on noise alone, not on an actual flaw in the system. Allowing 1 of 10 accepts that the system will occasionally get an honest writer wrong, while still keeping that rate low enough that it isn't the normal outcome.

---

## 2.

<!-- Your criterion. -->
`/submit` returns HTTP 400 with a JSON error body when `text` is missing, when `text` is an empty string (or whitespace-only), and when `text` exceeds 50,000 characters. It never returns a 500 or an unhandled crash for these three cases, across 5 of 5 tries each.

**Why this target:**
Unlike the scoring signals, input validation isn't probabilistic. The same bad input should fail the same way every time. A crash here isn't a near-miss on a hard case, it's a bug, and oversized input is the stage most likely to take down the whole service rather than just mislabel one piece of content.

---

## 3.

<!-- Your criterion. -->

Given 5 appeals against valid `content_id`s from prior submissions, status changes to `under_review` and a log entry is written in 5 of 5 times.

**Why this target:**

Status changing to `under_review` isn't optional, it's the only signal that tells an accused person their challenge was actually received, not silently dropped. Logging is just as important, without a record, there's no way to later audit whether appeals are being handled consistently or ignored. Neither of these rely on the model running, so there's no excuse for anything less than 5 of 5. If an appeal is ever lost or unlogged, that's a bug that needs to be fixed.

---

## 4.

<!-- Your criterion. -->

Given 10 submissions split as 3 clearly-human, 3 clearly-AI, and 4 borderline/mixed, all three values of the response's `guess` field (`human`/`ai`/`unsure`) appear at least once across the 10.

**Why this target:**
A detector that only ever says "human" or "ai" isn't offering a real middle ground, no matter what the docs claim. That would mean the thresholds in `scoring.py` are set so no input ever lands in the middle band, which is a real flaw worth catching early rather than finding out in unit 8 when a reader says they never once saw the honest answer. Testing across human, AI, and borderline text makes sure the check isn't rigged by only trying cases that were never going to be unsure anyway.

---

## 5.

<!-- Your criterion. -->
Given 5 clearly-human and 5 clearly-AI samples (10 total), at least 8 of 10 get the correct side: a human sample's `guess` isn't `"ai"`; an AI sample's `guess` isn't `"human"`; `"unsure"` counts as correct for either.

**Why this target:**
Criterion 1 only checks one direction: that human writing doesn't get falsely flagged as AI. It says nothing about whether the system actually catches AI text. A detector that leans lenient to protect criterion 1 could pass it while missing real AI text constantly, and that's not a system worth shipping either. 8 of 10 leaves room for the same run-to-run model noise criterion 1 accounts for, but still requires the system to get most cases right in both directions, not just avoid one kind of error.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
