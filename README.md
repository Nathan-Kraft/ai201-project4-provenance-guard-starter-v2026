# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

A submission moves through seven stages:

1. **Validation:** `/submit` checks that `text` is present, non-empty, and
   not oversized. Anything that fails stops here with a 400; nothing below
   runs.
2. **Model signal:** `detector.model_signal` runs the text through gpt2 and
   turns its perplexity into a 0-1 score: how predictable the text is to a
   language model.
3. **Style signal:** `stylometry.style_signal` measures sentence-length
   spread, vocabulary variety, and punctuation, and combines them into a
   second 0-1 score based on the shape of the text, not its meaning.
4. **Combining:** `scoring.combine_signals` merges the two scores into one,
   deciding how much weight each gets and what happens when they disagree.
5. **Labeling:** `scoring.score_to_label` turns that single score into a
   short tag (`ai` / `human` / `unsure`) and a sentence written for a reader
   who has never seen a threshold.
6. **Logging:** `audit.log_decision` writes every field of the decision
   (both signal scores, the combined score, the label) to the audit log,
   permanently.
7. **Response:** the same scores and label are returned to the caller, so
   the log and the response can never drift apart.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to gpt2, measured as perplexity. Low perplexity, meaning the model barely blinks at it, scores toward AI. High perplexity scores toward human.

**Why that might differ between human and AI writing:** A model writes by picking the likely next word over and over. So its own output tends to be easy for a model to predict. People don't write that way. They go off on tangents, pick an odd word, say something oddly specific instead of the typical thing.

**What it can't see:** Predictability isn't authorship. This signal rewards plain, ordinary sentences built from common words, so a second-language writer, a younger writer, or just someone who writes simply on purpose can score exactly as "AI" as a machine does. It cuts the other way too: dense, formal writing full of rare words usually reads as human here, since rare words are what the model finds hard to predict. The people most likely to get falsely accused by this signal are the ones least equipped to push back.

### Signal two — the style signal

**What it measures:** Not meaning, just shape. How much sentence length varies, how varied the vocabulary is, how much punctuation shows up.

**Why that might differ between human and AI writing:** Generated text tends to settle into even, mid-length sentences and a narrower vocabulary, since that's what picking the statistically likely word produces on average. Real writing is lumpier. A short sentence next to a long one.

**What it can't see:** It can't read. It has no idea what the text actually says, only what shape it's in. So anything that changes the shape without touching the meaning moves the score. Toss in a typo, break a sentence in half, paste in a quote. All cheap, all deliberate, and exactly what the attack set next unit is built to try.

### A calibration false positive

Milestone 4's four calibration inputs (clearly AI, clearly human, formal
human, lightly-edited AI) turned up a real false positive on the formal
human sample - a passage from a conducting textbook describing baton
technique. Both signals and their blind spots above are not abstract:

- **model_score: 0.7418** (leans AI). The passage explains a procedure
  in short, plain, declarative sentences built from common words -
  exactly the "predictable to a language model" blind spot named above,
  regardless of who wrote it.
- **style_score: 0.6539** (leans AI). Breaking this down:
  `sentence_length_spread` = 0.1584 raw (fairly even sentence lengths,
  reads as AI-ish), `type_token_ratio` = 0.5902 raw (varied vocabulary,
  correctly reads as human-ish), `punctuation_density` = 0.0145 raw
  (plain punctuation, reads as AI-ish). Two of the three measures
  misfire here, and the one that got it right is outvoted.
- **combined_score: 0.7110**, above `AI_THRESHOLD` (0.65), so this
  genuinely human, formally written passage is labeled high-confidence
  AI.

This is not a bug. It is the blind spots named in both signals above,
triggering on the same piece of text at the same time: plain,
procedural, explanatory writing is exactly what both signals mistake
for machine output.

### A near miss on the human label

The same calibration run turned up the opposite problem on the clearly
human sample - plain, straightforward writing that should be an easy
"human" call:

- **model_score: 0.4445.** Near the middle, not confidently human. The
  text is clear and well-constructed, which is exactly what reads as
  "predictable to a language model" - the same blind spot named above,
  just not severe enough here to push the score toward AI.
- **style_score: 0.2993** (leans human).
- **combined_score: 0.3937**, just above HUMAN_THRESHOLD (0.35), so this
  genuinely human sample is labeled unsure instead of human.

This is not a bug either. It's the model signal's blind spot showing up
on the human side instead of the AI side: plain, fluent writing reads as
predictable regardless of who wrote it. Here the result is a missed
"human" call rather than a false accusation of AI - arguably the safer
direction to be wrong in, but still a limitation worth naming rather
than hiding behind a threshold picked to avoid it.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

Both signals are 0-1 scores where higher means more likely AI. If they
disagree by more than a set amount, that counts as a genuine split
rather than a close call, and the combined score is forced to 0.5
(unsure) instead of being averaged. Otherwise, the combined score is a
weighted average of the two, with the model signal weighted more
heavily than the style signal.

**The numbers:**

- `WEIGHT_MODEL_SIGNAL = 0.65`
- `WEIGHT_STYLE_SIGNAL = 0.35`
- `DISAGREEMENT_GAP_THRESHOLD = 0.4` (if `abs(model_score - style_score)`
  is above this, the combined score is forced to 0.5 instead of averaged)

Model gets more weight than style because testing across six samples
showed style_score staying close to 0.5 on every one of them
(0.31-0.54), while model_score moved widely (0.23-0.89). A signal that
barely moves shouldn't carry equal weight with one that does.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

The "evasion_typos" sample: model_score 0.2323 (leans human),
style_score 0.5299 (leans AI). The gap between them is 0.2976, under the
0.4 threshold, so the rule falls back to the weighted average instead of
forcing unsure. That average lands at 0.3365, below HUMAN_THRESHOLD
(0.35), so the combined guess reads as human: the model signal's
stronger lean toward human outweighs the style signal's weak lean
toward AI.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | score < 0.35 | Our system's best guess is that this was written by a person, not generated by AI. |
| unsure | 0.35 to 0.65 | We can't confidently tell whether this was written by a person or by AI. |
| high-confidence AI | score > 0.65 | Our system's best guess is that this was generated by AI, not written by a person. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl.exe -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d @samples/clearly_ai.json
```

```json
{
  "confidence": 0.5,
  "content_id": "c_76c2f703f021",
  "guess": "ai",
  "label": "Our system's best guess is that this was generated by AI, not written by a person.",
  "model_score": 0.7544,
  "style_score": 0.530663297760872
}
```

**An appeal**

```bash
$ curl.exe -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d "{\"content_id\": \"c_76c2f703f021\", \"reasoning\": \"I wrote this myself for a work training handout, I did not use AI.\"}"
```

```json
{
  "content_id": "c_76c2f703f021",
  "message": "Your appeal has been recorded. A person will review this submission.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl.exe "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.6760921542163052,
      "content_id": "c_76c2f703f021",
      "creator_id": "demo_instructor",
      "guess": "ai",
      "label": "Our system's best guess is that this was generated by AI, not written by a person.",
      "model_score": 0.7544,
      "status": "decided",
      "style_score": 0.530663297760872,
      "timestamp": "2026-11-09T04:13:05+00:00"
    },
    {
      "content_id": "c_76c2f703f021",
      "creator_id": "demo_instructor",
      "event": "appeal",
      "reasoning": "I wrote this myself for a work training handout, I did not use AI.",
      "status": "under_review",
      "timestamp": "2026-11-09T04:15:42+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Help designing `combine_signals` after finding a split
  case (the evasion_typos sample, where model_score leaned human and
  style_score leaned AI). I wanted a way to weight the two signals that
  accounted for how much they disagreed.
- *What came back:* A continuous, disagreement-dependent weighting formula,
  where the gap between the two signals would scale their relative weight.
- *What I changed:* Decided against the continuous formula, since no single
  fixed weight could give both "the model signal carries more weight on
  close calls" and "opposite extremes count as unsure" at the same time.
  Used a simpler two-part rule instead: a plain weighted average normally,
  with a hard override to 0.5 when the gap exceeds
  `DISAGREEMENT_GAP_THRESHOLD`.

**Moment 2**

- *What I asked for:* To wire `detector.model_signal` into `/submit` using
  the existing draft of the route.
- *What came back:* A version with validation, the detector call, and the
  audit log call present, but in the wrong order. The detector call and
  audit log ran before the missing/empty `text` check, so a bad request
  would hit `detector.model_signal(None)` before the 400 check ever ran.
- *What I changed:* Reordered the route so validation runs first and
  returns 400 immediately, before the detector or audit log ever execute.

## Stretch Features

### Stretch: `GET /content/<id>`

**Declared before building:** adds a read-only endpoint that returns one
submission's current status by `content_id`. It looks up the most recent
entry for that id in the audit log (the original decision, or
`under_review` if an appeal was filed) without re-running either signal.
Returns 404 for an unknown `content_id`, matching `/appeal`'s existing
behavior.

**What it looks like:**

```bash
$ curl.exe http://127.0.0.1:5000/content/c_c52d6efa16b9
```

```json
{
  "combined_score": 0.6760921542163052,
  "content_id": "c_c52d6efa16b9",
  "guess": "ai",
  "label": "Our system's best guess is that this was generated by AI, not written by a person.",
  "model_score": 0.7544,
  "status": "decided",
  "style_score": 0.530663297760872
}
```

After an appeal against the same content_id, the same request returns
`"status": "under_review"` with the rest unchanged - the original
guess/label/scores are preserved, not recomputed.

An unknown content_id returns 404:

```json
{
  "error": "not_found",
  "message": "No submission found with content_id 'does_not_exist'."
}
```

### Stretch: A third signal (burstiness)

**Declared before building:** adds a third 0-1 score, `burstiness_signal`,
measuring how much the text's local predictability varies, rather than its
average (which `detector.model_signal` already measures). Splits the text
into sentences, runs each one through the same gpt2 perplexity measurement
used in signal one, and takes the variance across those per-sentence
readings. Human writing tends to swing between very predictable and very
surprising sentences; AI output tends to stay uniformly smooth. Blind
spot: fewer than two sentences gives no variance to measure, and a short
submission's reading will be noisy regardless of the text.

(This replaces a specificity signal declared and partly built first -
counting numerals and proper nouns per word. Calibration testing showed it
saturated to the most extreme "AI" reading on nearly every sample lacking
a name or a number, including plainly human and even deliberately AI
samples, which worked against the project's priority of minimizing false
accusations. Dropped before it was wired into `combine_signals`.)

Combined into `scoring.py::combine_signals` alongside the existing two
signals: the same weighted-average-with-disagreement-override shape,
extended to three weights that sum to 1. Exact weights will be set by
calibration against the existing sample set, the same way
`WEIGHT_MODEL_SIGNAL`/`WEIGHT_STYLE_SIGNAL` were, and documented here once
chosen.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
