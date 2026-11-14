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

### A third signal (not pursued)

A third signal was attempted twice: first specificity (numerals and
proper nouns per word), then burstiness (variance in per-sentence
perplexity). Both were declared and calibration-tested before being
wired into `combine_signals`. Specificity saturated to the most extreme
AI reading on nearly every sample lacking a name or number in it,
including human and AI samples alike. Burstiness avoided that saturation
problem but didn't rank the calibration samples in a sensible order
(`clearly_ai` scored less AI-like than `lightly_edited_ai`), so a low
weight would have made it harmless but also uninformative. Dropped in
favor of spending the remaining time on Unit 8's required work. Full
detail in git history.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

If a person was submitting their work they probably wouldn't have more than 50 a day, as well as they would be only submitting a few an hour. Which should keep them well under the 5 per minute rule. A script that sends thousand variations gets cut off after 5 requests in a minute, so it can't gather much data before being throttled.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

Per `creator_id`, not per IP address. `rate_limit_key` in app.py reads `creator_id` from the request body and keys the limit on that, only falling back to the caller's IP address if `creator_id` is missing or not a string. This matters because a script can rotate IPs but still count as one caller if it reuses a `creator_id`, while a household sharing one IP isn't throttled as a single caller.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 429
  [ 7/15] 429
  [ 8/15] 429
  [ 9/15] 429
  [10/15] 429
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================

10 of 15 were rate limited.
```

Note: this run was logged before the audit log fix below — its rejected
entries in logs/audit.jsonl are missing the decision fields (content_id,
guess, model_score, style_score, combined_score, label). A later run shows
rejected entries with all nine fields present as null.

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_89d203bf5bcf` | unsure | 0.500 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_02fa97168856` | unsure | 0.500 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_7ad2a3623c1b` | unsure | 0.500 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_a7317d8fe33d` | unsure | 0.500 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_1c17ace0a0a9` | unsure | 0.500 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_8d0bbbc1f2b4` | unsure | 0.500 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_cf9b98ae20ab` | unsure | 0.500 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `c_5c51d32f1116` | unsure | 0.500 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_47e51130e501` | unsure | 0.500 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_3db7ebe693ee` | ai | 0.500 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_8a5d571092a8` | unsure | 0.500 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c_1e9c7392b68e` | ai | 0.500 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_db651cd2b649` | ai | 0.500 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_6d2545e920e2` | ai | 0.500 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_e7dd9bb93920` | ai | 0.500 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_34d38d2624ef` | ai | 0.500 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_d472a0a8ddc3` | ai | 0.500 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `c_651fbf18adbd` | unsure | 0.500 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_4b89e789dd26` | unsure | 0.500 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_cd7059b968a9` | human | 0.500 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_4523edd4b79f` | unsure | 0.500 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_b57e1017241b` | unsure | 0.500 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_3dad31aa5562` | unsure | 0.500 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_5b1d6baca6c7` | unsure | 0.500 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `c_891c35e06447` | unsure | 0.500 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `c_f0b95ae7b277` | unsure | 0.500 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `c_b3be8d665dc0` | ai | 0.500 | HELD |
| MF06 | malformed | text is emoji only | 200 | `c_cc78d8967938` | ai | 0.500 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `c_7056a71f657b` | ai | 0.500 | BROKE |
| MF08 | malformed | text is 60,000 characters | 200 | `c_6589cbf90dfc` | ai | 0.500 | BROKE |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `c_c3f163db5a44` | unsure | 0.500 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `c_0486ee09a260` | unsure | 0.500 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | N/A — blocked by the rate limiter before the route ran |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | N/A — blocked by the rate limiter before the route ran |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_6cc66865b58d` | unsure | 0.500 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_4b7f541eccff` | unsure | 0.500 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_f88f0854cad5` | unsure | 0.500 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_e98d968c8b62` | unsure | 0.500 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_63d4cb6000e8` | unsure | 0.500 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

11 BROKE, 2 N/A (blocked by the rate limiter before the route ran), 43 HELD.

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-13T22:59:06+00:00", "content_id": "c_1e9c7392b68e", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.6690652288553305, "combined_score": 0.7143278300993657, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "status": "decided"}
{"timestamp": "2026-11-13T22:59:06+00:00", "content_id": "c_db651cd2b649", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.6496398516315162, "combined_score": 0.7506889480710307, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "status": "decided"}
{"timestamp": "2026-11-13T22:59:06+00:00", "content_id": "c_6d2545e920e2", "creator_id": "attacker_FP04", "guess": "ai", "model_score": 0.8329, "style_score": 0.5931167816382161, "combined_score": 0.7489758735733756, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "status": "decided"}
{"timestamp": "2026-11-13T22:59:06+00:00", "content_id": "c_e7dd9bb93920", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.6785390272349948, "combined_score": 0.7578136595322482, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "status": "decided"}
{"timestamp": "2026-11-13T22:59:07+00:00", "content_id": "c_34d38d2624ef", "creator_id": "attacker_FP06", "guess": "ai", "model_score": 0.8814, "style_score": 0.5632679282571954, "combined_score": 0.7700537748900185, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "status": "decided"}
{"timestamp": "2026-11-13T22:59:07+00:00", "content_id": "c_d472a0a8ddc3", "creator_id": "attacker_FP07", "guess": "ai", "model_score": 0.8816, "style_score": 0.5640190465472043, "combined_score": 0.7704466662915216, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "status": "decided"}
{"timestamp": "2026-11-13T22:59:07+00:00", "content_id": "c_cd7059b968a9", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.42279527511411846, "combined_score": 0.2808383462899414, "label": "Our system's best guess is that this was written by a person, not generated by AI.", "status": "decided"}
{"timestamp": "2026-11-13T22:59:08+00:00", "content_id": "c_7056a71f657b", "creator_id": "attacker_MF07", "guess": "ai", "model_score": 0.9064, "style_score": 1.0, "combined_score": 0.93916, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "status": "decided"}
{"timestamp": "2026-11-13T22:59:09+00:00", "content_id": "c_6589cbf90dfc", "creator_id": "attacker_MF08", "guess": "ai", "model_score": 0.9876, "style_score": 0.8296738770692907, "combined_score": 0.9323258569742519, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "status": "decided"}
{"timestamp": "2026-11-13T22:59:09+00:00", "content_id": null, "creator_id": "attacker_flood", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

FP03 — a non-native English speaker writing carefully, confidently called AI
(combined_score 0.7507). This is the one I'd least want to explain: a real
person doing their best in a second language, penalized by the exact pattern
documented in real-world AI-detector research — careful, simpler non-native
phrasing reads to the model like AI output. Telling that writer "our system
is confident you didn't write this" isn't a coin-flip miss, it's the system
working exactly as built and still landing on the writer least able to
push back.

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
