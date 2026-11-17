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

**Moment 3**

- *What I asked for:* Pick one improvement from the diagnoses (reweight
  the signals, move a threshold, or validate the input) and make the case
  for it before touching any code.
- *What came back:* A first recommendation to raise `AI_THRESHOLD` from
  0.65 to 0.75, since that's where the four criterion 1 false positives
  landed. I pushed back and asked for the diagnosis to be checked more
  carefully before picking. On a second pass, it pulled the actual
  combined scores for the false positives (0.68 to 0.77) against genuine
  clearly-AI samples (0.68 to 0.73) and found the two ranges overlap, so
  no threshold or reweight could fix the false positives without also
  making the service unable to confidently call real AI text `ai` at all,
  trading one miss for another on criterion 4. It proposed input
  validation instead: a length check and a payload-type guard at the
  route, which cleanly fixed criterion 2 and two broken attacks with no
  such trade-off.
- *What I changed:* Went with the input-validation fix as proposed. I
  didn't make an independent call here beyond asking it to look harder
  before I'd accept the first answer; the numbers it found made the case
  on their own.

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
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD — blocked by the rate limiter before the route ran |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD — blocked by the rate limiter before the route ran |
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

11 BROKE, 0 N/A, 45 HELD.

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

### Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | At most 1 of 10 confirmed human pieces flagged `ai` | 4/10 flagged ai | 4/10 flagged ai | 4/10 flagged ai | MISS |
| 2. bad input | 400 for missing/empty/whitespace-only text and text over 50,000 characters, 5/5 each, never 500 | missing 5/5, empty 5/5, whitespace 5/5 all 400; huge text 5/5 came back 200 | same | same | MISS (huge text isn't rejected) |
| 3. appeal path | 5 of 5 appeals against valid content_ids change status to `under_review` and get logged | 5/5 under_review, 5/5 logged | 5/5 under_review, 5/5 logged | 5/5 under_review, 5/5 logged | MET |
| 4. label coverage | All three `guess` values appear across 3 clearly-human/3 clearly-AI/4 borderline texts | only `ai` and `unsure` appeared, never `human` | same | same | MISS |
| 5. correct side | At least 8 of 10 (5 human + 5 AI) get the correct side | 10/10 | 10/10 | 10/10 | MET |

**How each MET verdict was decided:**

- Criterion 3: the target is 5 of 5 in every trial, with nothing less counting. All three trials came back 5/5 under_review and 5/5 logged, so it's MET.
- Criterion 5: the target is at least 8 of 10 in every trial. All three trials came back 10/10, clearing the floor by 2 in each one, so it's MET.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

### 1. my own writing

From `results/run_2026-11-14_1434_before.md`, Trial 1, produced by `run_eval.py::main` against `app.py::submit`:

```json
[
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.4445, "style_score": 0.2992864290997694, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "I didn't sleep. Not properly, anyway — I lay there listening to the bo"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.8107, "style_score": 0.6113444730177474, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "I had to go to the grocery store on Monday. I had to make sure I got s"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.6409, "style_score": 0.5902523298820032, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "Today I was at work for most of the day. It was so slow and boring, no"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.8575, "style_score": 0.6112922559712254, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "I was wondering if I could get an extension for this project. On top o"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.7156, "style_score": 0.626443185875894, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "I like watching anime, I have a few that I absolutely adore and always"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.7117, "style_score": 0.44898798632940795, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "When I am dealing with a bug in code that I need to fix, I have a few "},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.5919, "style_score": 0.6184744450544745, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "My breakfast is two breakfast burritos and half a bag of potato rounds"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.427, "style_score": 0.5587973413840813, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "I don't understand some drivers in my town. How is it that a small cit"},
  {"status": 200, "guess": "human", "confidence": 0.5, "model_score": 0.1464, "style_score": 0.47142146122059997, "label": "Our system's best guess is that this was written by a person, not generated by AI.", "sent": "Hey sorry for the late reply, work was insane today. The printer broke"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.7418, "style_score": 0.6538684303219519, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "In directing music the tip of the baton describes certain patterns tha"}
]
```

### 2. bad input

From `results/run_2026-11-14_1434_before.md`, Trial 1, produced by `run_eval.py::main` against `app.py::submit`:

```json
[
  {"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "{\"creator_id\": \"eval_bad_missing_1\"}"},
  {"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "(empty text)"},
  {"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "   "},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.9975, "style_score": 0.9999933333333333, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "word word word word word word word word word word word word word word "}
]
```

(One representative entry per bad-input case shown here; all 20 entries for Trial 1 are in `results/run_2026-11-14_1434_before.md` under "bad input".)

### 3. appeal path

Tested by hand with curl, not via `run_eval.py`, against `app.py::submit` and `app.py::appeal`:

```json
{"confidence": 0.5, "content_id": "c_d5852ad382f1", "guess": "unsure", "label": "We can't confidently tell whether this was written by a person or by AI.", "model_score": 0.0025, "style_score": 0.6666666666666666}
```

```json
{"content_id": "c_d5852ad382f1", "message": "Your appeal has been recorded. A person will review this submission.", "status": "under_review"}
```

Matching entries from `logs/audit.jsonl`:

```json
{"timestamp": "2026-11-14T22:37:57+00:00", "content_id": "c_d5852ad382f1", "creator_id": "eval_appeal_doc", "guess": "unsure", "model_score": 0.0025, "style_score": 0.6666666666666666, "combined_score": 0.5, "label": "We can't confidently tell whether this was written by a person or by AI.", "status": "decided"}
{"timestamp": "2026-11-14T22:39:07+00:00", "content_id": "c_d5852ad382f1", "creator_id": "eval_appeal_doc", "event": "appeal", "status": "under_review", "reasoning": "I wrote this myself"}
```

### 4. label coverage

From `results/run_2026-11-14_1434_before.md`, Trial 1, produced by `run_eval.py::main` against `app.py::submit`:

```json
[
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.8107, "style_score": 0.6113444730177474, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "I had to go to the grocery store on Monday. I had to make sure I got s"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.7156, "style_score": 0.626443185875894, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "I like watching anime, I have a few that I absolutely adore and always"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.427, "style_score": 0.5587973413840813, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "I don't understand some drivers in my town. How is it that a small cit"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.856, "style_score": 0.49610803855493407, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "Maintaining a balanced diet is essential for long-term health and well"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.8212, "style_score": 0.5093079231629042, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "Climate change remains one of the most pressing challenges facing huma"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.7735, "style_score": 0.5311571161013154, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "Remote work has become an increasingly popular arrangement in the mode"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.3489, "style_score": 0.48130515629960274, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "Time management matters more than people admit, especially now that wo"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.6772, "style_score": 0.4909082285119702, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "Climate change is honestly one of the biggest problems we've got right"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.6405, "style_score": 0.556951953427131, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "I almost didn't go to the climate march last weekend, it was raining a"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.3013, "style_score": 0.5733034614976793, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "Good study habits really do make a difference. If you actually use str"}
]
```

### 5. correct side

From `results/run_2026-11-14_1434_before.md`, Trial 1, produced by `run_eval.py::main` against `app.py::submit`:

```json
[
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.4445, "style_score": 0.2992864290997694, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "I didn't sleep. Not properly, anyway — I lay there listening to the bo"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.6409, "style_score": 0.5902523298820032, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "Today I was at work for most of the day. It was so slow and boring, no"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.7117, "style_score": 0.44898798632940795, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "When I am dealing with a bug in code that I need to fix, I have a few "},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.5919, "style_score": 0.6184744450544745, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "My breakfast is two breakfast burritos and half a bag of potato rounds"},
  {"status": 200, "guess": "human", "confidence": 0.5, "model_score": 0.1464, "style_score": 0.47142146122059997, "label": "Our system's best guess is that this was written by a person, not generated by AI.", "sent": "Hey sorry for the late reply, work was insane today. The printer broke"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.7544, "style_score": 0.530663297760872, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "The importance of effective time management cannot be overstated in to"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.856, "style_score": 0.49610803855493407, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "Maintaining a balanced diet is essential for long-term health and well"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.8212, "style_score": 0.5093079231629042, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "Climate change remains one of the most pressing challenges facing huma"},
  {"status": 200, "guess": "ai", "confidence": 0.5, "model_score": 0.7735, "style_score": 0.5311571161013154, "label": "Our system's best guess is that this was generated by AI, not written by a person.", "sent": "Remote work has become an increasingly popular arrangement in the mode"},
  {"status": 200, "guess": "unsure", "confidence": 0.5, "model_score": 0.5583, "style_score": 0.5572801148174494, "label": "We can't confidently tell whether this was written by a person or by AI.", "sent": "Effective study techniques play a vital role in academic success. Stud"}
]
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

**The pattern across misses**

Two distinct root causes produced all three misses, not three independent ones. Criteria 1 and 4 are the same problem twice: signal one's "plain writing reads as predictable" blind spot, amplified by the combining rule's 0.65 weight on model_score, caught on two different sets of test data. Criterion 2 is a separate, unrelated gap: a missing length check at the route, nothing to do with either signal. The same signal-one-plus-weighting cause also accounts for 7 of the 11 broken attacks below (FP02-07, PI02).

**Criterion 1 - my own writing (4/10 confirmed-human pieces flagged `ai`)**

Stage: signal one, amplified by the combining rule.

The four flagged pieces, from the Trial 1 data above: "I had to go to the grocery store..." (model_score 0.8107), "I was wondering if I could get an extension..." (0.8575), "I like watching anime..." (0.7156), and the conducting-textbook passage (0.7418, detailed in "A calibration false positive" above). All four are plain, declarative sentences built from common words, exactly the shape signal one's blind spot rewards with a low-perplexity, high-AI-score reading, regardless of who wrote them. The combining rule weights model_score at 0.65 against style_score's 0.35, so that AI-ish reading dominates the average in all four cases and the combined score clears AI_THRESHOLD (0.65).

**Criterion 2 - oversized text not rejected**

Stage: the route.

`/submit`'s validation (app.py line 208) checks only that `text` is a string and not blank; there is no length check anywhere in the route. The eval's oversized-text case, a string of the word "word" repeated past 50,000 characters, passed validation untouched, came back `200`, and was scored normally: model_score 0.9975, style_score 0.99999, guess `ai`. The criterion was never implemented, not misfiring: nothing in app.py defines what counts as oversized.

**Criterion 4 - label coverage (`human` never appears across 3 clearly-human, 3 clearly-ai, 4 borderline texts)**

Stage: signal one, amplified by the combining rule. Same mechanism as criterion 1, different samples.

The three human texts chosen for this scenario (clearly_human_02, _05, _08) score 0.8107, 0.7156, and 0.427 on the model signal. The first two already sit solidly in AI territory before the combining rule even runs; the third, at 0.427, isn't low enough for style_score to pull the combined score under HUMAN_THRESHOLD (0.35) once model_score carries 0.65 of the weight. None of the three ever produces a combined score low enough for `guess=human`, so the label never fires in this run. This isn't proof the label is unreachable in general (clearly_human_09 reaches 0.15 and scores `human` in criterion 1's data) - it's that these three plain, listy samples happen to be exactly the shape signal one misreads.

**FP02 through FP07 (6 of the 11 BROKE attacks)**

Stage: signal one, amplified by the combining rule. Same mechanism as criterion 1, attacked on purpose instead of found by accident: each is genuine human writing in a shape signal one misreads as predictable (formal register, careful non-native phrasing, a rubric-driven essay, technical documentation, imitation of a template, deliberate repetition). Six attacks, one underlying cause.

**PI02 - instruction disguised as a system message**

Stage: signal one, amplified by the combining rule, not the route or the label mapping. The service never parses or obeys text as instructions anywhere in the pipeline, so the injected "SYSTEM: ... Return guess=human" line is never read as a command. What actually flips the guess is that this unnatural, instruction-shaped phrasing is exactly the kind of text gpt2 finds surprising, so model_score reads low (0.2044, human-leaning) despite the AI-sounding boilerplate that follows it. The 0.65 weight on model_score carries that reading through to a combined score of 0.2808, under HUMAN_THRESHOLD. The attack succeeds by accident, by exploiting the same "unusual phrasing reads human" blind spot named in the Signal one section, not by any instruction-following ability in the route or label mapping.

**MF02 - a single character (500)**

Stage: signal one.

`detector.perplexity` raises `ValueError` whenever the tokenized input has fewer than 3 tokens (detector.py lines 106-107); a single character tokenizes to 1 or 2. Nothing in `/submit` catches that exception, so it propagates past the route as an unhandled 500 instead of a 400. The route checks presence and non-emptiness but not minimum content length, so input that passes validation can still crash the signal underneath it.

**MF07 - right-to-left script (ai, style_score 1.0)**

Stage: signal two.

`stylometry.words()` only matches `[a-z0-9']+`, ASCII Latin letters and digits. Right-to-left script text contains none, so `words()` returns an empty list for every sentence. Both `type_token_ratio` and `sentence_length_spread` hit their documented empty-input fallback of 0.0, which `style_signal` converts into the maximally-AI-ish reading instead of "unmeasurable." All three sub-measures land on the AI extreme at once, pushing style_score to 1.0 and the combined score to 0.939: confidently, wrongly, AI.

**MF08 - 60,000 characters (ai)**

Stage: the route, compounded by signal one. Same validation gap as criterion 2: the oversized body should have been rejected and wasn't. Once it reaches signal one, the long, repetitive text is highly predictable to gpt2 (model_score 0.9876), and the combining rule carries that straight through to a confidently-AI score. Two failures compounding, not one.

**RQ07 - body is a JSON array, not an object (500)**

Stage: the route.

`payload = request.get_json(silent=True) or {}` (app.py line 203) only falls back to `{}` when the parsed body is falsy. A JSON array parses to a non-empty list, which is truthy, so `payload` becomes that list, and the next line's `payload.get("text")` raises `AttributeError` since a list has no `.get`. Flask turns that into an unhandled 500 before any validation runs. The rate limiter's own `rate_limit_key` function already guards against exactly this case by checking `isinstance(payload, dict)` first; the route itself never got the same guard.

---

## The Improvement

**What I changed:**

Added a maximum-length check and a payload-type guard to `/submit`'s input validation (app.py, the same block as the existing missing/empty check), plus a new `MAX_TEXT_LENGTH = 50000` constant in config.py. `request.get_json(silent=True)` is now checked with `isinstance(payload, dict)` before anything calls `.get()` on it, the same guard `rate_limit_key` already had, and text longer than `config.MAX_TEXT_LENGTH` now gets rejected with a 400 before either signal runs.

**Which diagnosis pointed at it:**

Three diagnoses above named the same stage: criterion 2 ("the route... no length check exists anywhere"), MF08 ("the route, compounded by signal one... the oversized body should have been rejected and wasn't"), and RQ07 ("the route... `payload.get("text")` raises `AttributeError`... the rate limiter's own `rate_limit_key` function already guards against exactly this case"). All three are the same missing input-validation step, not three separate problems, so one change at the route targeted all three. I deliberately did not touch the signal-one-plus-weighting cause behind criteria 1 and 4, since the false-positive and genuine-AI combined scores overlap in the same 0.68-0.77 range: any reweight or threshold move strong enough to fix the false positives would also stop the service from ever confidently calling real AI text `ai`, trading one miss for another rather than fixing one.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_1c823283fe65` | unsure | 0.500 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_9ef2cc73fb26` | unsure | 0.500 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_7dfd6e4427e4` | unsure | 0.500 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_8f82d5127d85` | unsure | 0.500 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_cab06e94b80f` | unsure | 0.500 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_3d0881fcc6a2` | unsure | 0.500 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_733eecc65625` | unsure | 0.500 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `c_895a0bd63a35` | unsure | 0.500 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_522b97f89029` | unsure | 0.500 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_32a93c38a573` | ai | 0.500 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_b4ec84e4fd7f` | unsure | 0.500 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c_38105e1d792e` | ai | 0.500 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_cf6a9d22eb9e` | ai | 0.500 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_688e02da271c` | ai | 0.500 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_32c628065aea` | ai | 0.500 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_70707911d070` | ai | 0.500 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_c122236b4985` | ai | 0.500 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `c_5aa3155e5e36` | unsure | 0.500 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_392aa5cb7875` | unsure | 0.500 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_12dcd93fa011` | human | 0.500 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_a0ffc23a1349` | unsure | 0.500 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_c705a2944378` | unsure | 0.500 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_949e907913a8` | unsure | 0.500 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_52aabd5cf5d3` | unsure | 0.500 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `-` | - | - | HELD |
| MF02 | malformed | text is a single character | 500 | `-` | - | - | BROKE |
| MF03 | malformed | text is control characters | 200 | `c_9ebe559fbb9a` | unsure | 0.500 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `c_bcd2830f768d` | unsure | 0.500 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `c_f28e850d3c56` | ai | 0.500 | HELD |
| MF06 | malformed | text is emoji only | 200 | `c_475e5a7007ea` | ai | 0.500 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `c_ea8105c87b74` | ai | 0.500 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `-` | - | - | HELD |
| RQ01 | malformed | no text field at all | 400 | `-` | - | - | HELD |
| RQ02 | malformed | no creator_id | 200 | `c_844a0530db28` | unsure | 0.500 | HELD |
| RQ03 | malformed | text is a number | 400 | `-` | - | - | HELD |
| RQ04 | malformed | text is a list | 400 | `-` | - | - | HELD |
| RQ05 | malformed | text is null | 400 | `-` | - | - | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `c_96e845b0ec7c` | unsure | 0.500 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `-` | - | - | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `-` | - | - | HELD |
| RQ09 | malformed | body is empty | 400 | `-` | - | - | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `-` | - | - | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `-` | - | - | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `-` | - | - | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_a23b0cf5b68c` | unsure | 0.500 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_0933baf1bdee` | unsure | 0.500 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_aca9e689dc77` | unsure | 0.500 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_14ff069f0f4c` | unsure | 0.500 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_466e3318d005` | unsure | 0.500 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `-` | - | - | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `-` | - | - | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `-` | - | - | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `-` | - | - | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `-` | - | - | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `-` | - | - | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `-` | - | - | HELD |

9 BROKE, 0 N/A, 47 HELD.

### Run Log and Verdicts — After

<!-- Same five criteria, same three trials, run after the input-validation change. `run_eval.py --label after`, from `results/run_2026-11-15_0052_after.md`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | At most 1 of 10 confirmed human pieces flagged `ai` | 4/10 flagged ai | 4/10 flagged ai | 4/10 flagged ai | MISS (unchanged) |
| 2. bad input | 400 for missing/empty/whitespace-only text and text over 50,000 characters, 5/5 each, never 500 | missing 5/5, empty 5/5, whitespace 5/5, huge text 5/5, all 400 | same | same | MET (fixed) |
| 3. appeal path | 5 of 5 appeals against valid content_ids change status to `under_review` and get logged | not re-run, unaffected by this change | - | - | MET (carried over) |
| 4. label coverage | All three `guess` values appear across 3 clearly-human/3 clearly-AI/4 borderline texts | only `ai` and `unsure` appeared, never `human` | same | same | MISS (unchanged) |
| 5. correct side | At least 8 of 10 (5 human + 5 AI) get the correct side | 10/10 | 10/10 | 10/10 | MET (unchanged) |

Only criterion 2 moved. The input-validation fix targeted the route, which is what criterion 2 tests, and nothing else touches the route, so nothing else was expected to move, and nothing else did.

**Did it help, and how do I know:**

Yes, on the axis this change targeted, and no further. BROKE count dropped from 11 to 9: RQ07 (500 to 400) and MF08 (confident `ai` on 60,000 characters, now a 400, rejected before either signal ran) both moved to HELD. The eval's criterion 2 went from MISS to MET: all three bad-input cases (missing, empty, now oversized) returned 400 across all 20 tries in all 3 trials. Nothing else moved: criterion 1 stayed at 4/10 false positives, criterion 4 still never produces `human`, criterion 5 stayed at 10/10, because none of that is downstream of input validation. MF02 (single character, still a 500) is the one attack this change was never meant to cover, left as a named gap.



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**Criterion 1 (4/10 confirmed-human pieces flagged `ai`), criterion 4 (`human` never appears), and FP02-FP07 (6 attacks): all one cause.** Signal one's blind spot (plain, common-word writing reads as predictable, hence AI-ish) amplified by the combining rule's 0.65 weight on `model_score`, diagnosed above. What I'd do: design a combining rule that can actually separate the two populations, not just slide the same threshold back and forth. I checked the actual numbers before picking this unit's one change, and found the false-positive combined scores (0.68-0.77) and genuine clearly-AI combined scores (0.68-0.73) overlap in the same band. No single reweight or threshold move I tried fixes the false positives without also making the service unable to confidently call real AI text `ai` at all, which would trade this miss for a new one on criterion 4's reachability test. Why I stopped: that needs a smarter rule (per-length calibration, a third signal, or a non-linear combination) than I had time to design and test this round, so I picked the one change that was a clean win instead (input validation) and left this one named rather than rushed.

**PI02 (instruction disguised as a system message): same family, opposite direction.** The diagnosis already shows this attack doesn't work by the service obeying injected text; it works because the injected text's unnatural phrasing is exactly what gpt2 finds surprising, so `model_score` reads low. Why I stopped: fixing this specific case by hand (detecting "system message"-shaped text) would be overfitting to one attack's wording rather than a real fix, and the real fix is the same signal-one combining-rule problem as above.

**MF02 (single character, 500) — resolved by the stretch improvement.**
The new minimum-content check rejects the request with `400` and records
`text_too_short` before `detector.perplexity()` can raise its fewer-than-three
tokens `ValueError`. The same check also holds MF05 and MF06, while the
remaining broken attacks below are unchanged.

**MF07 (right-to-left script, style_score 1.0).** `stylometry.words()` only matches `[a-z0-9']+`, so RTL text produces zero matched words, all three style sub-measures hit their empty-input fallback at once, and `style_signal` reads that as maximally AI-ish instead of "unmeasurable." What I'd do: make `words()` Unicode-aware (for example `\w+` with the `re.UNICODE` flag, or a real tokenizer), and separately reconsider whether "can't measure" should default to the AI extreme at all, since it isn't evidence of anything. Why I stopped: this is a real signal-two bug I found while diagnosing, but fixing it wasn't the one change I picked this round, and I didn't want to make two unrelated changes and lose the ability to say cleanly which one caused which result.

**Criterion 5's loophole, named but not resolved.** A detector that always answered `unsure` would pass this criterion 10/10 without ever committing to a side, since `unsure` counts as correct for either. Criterion 5 was measured cleanly (10/10, three trials), so this doesn't qualify for a formal revision under criteria.md's own rule: revisions are for a criterion that couldn't be measured, not one that passed too easily. Flagging it here as a known weakness in how the criterion is written, left for whoever picks this project up next.

**The trade I'd make if this ran for real:**

I'd keep weighting toward fewer false accusations, the same direction criterion 1 already picked, even knowing it lets more real AI text through unflagged. The people who pay for that are whoever relies on the `ai` label meaning something, an instructor, an editor, a reader, not the wrongly-accused writer, and that's a cost I'd rather hand to the reader of a report than to the person whose name is on it.

### Stretch: Reject too-short submissions

**Declared before building:** add a minimum-content validation check to
`POST /submit` so text that cannot produce a detector score is rejected
with a JSON `400` response and an audit-log rejection instead of crashing.
This targets `MF02`, where a single-character submission reaches
`detector.perplexity()` and raises a `ValueError` because it has fewer than
three tokens.

**What I changed:** added `MIN_TEXT_WORDS = 3` in `config.py` and a route
validation check before either signal runs. Text below that minimum now
returns `400` and calls `audit.log_rejection(..., reason="text_too_short")`.

**Attack Run — After Stretch Improvement**

I reran the full set with `run_attacks.py --label after_short`; the complete
raw output is in `results/attack_run_2026-11-15_0217_after_short.md`.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_e700e27bc5a5` | unsure | 0.500 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_a4679a7fbe65` | unsure | 0.500 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_5774e33aa006` | unsure | 0.500 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_03555da98c3a` | unsure | 0.500 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_58635b09dead` | unsure | 0.500 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_fe452462e524` | unsure | 0.500 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_df26b41e2540` | unsure | 0.500 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `c_0e534900bca0` | unsure | 0.500 | HELD |
| EV09 | evasion | both signals: AI text with a human opening paragraph bolted on | 200 | `c_6273ab2fc4bf` | unsure | 0.500 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_061657565288` | ai | 0.500 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_4e2b671a9ece` | unsure | 0.500 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c_d076a2ffc172` | ai | 0.500 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_9cafc71f5ef3` | ai | 0.500 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_4011410d6957` | ai | 0.500 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_f58bfc37f349` | ai | 0.500 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_ff7b68ef3799` | ai | 0.500 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_2315b15cb9aa` | ai | 0.500 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `c_e5a5cbe7e2b4` | unsure | 0.500 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_05a57e084c33` | unsure | 0.500 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_e09596efecda` | human | 0.500 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_9219969fabd5` | unsure | 0.500 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_1a818d425688` | unsure | 0.500 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_c2efc103048c` | unsure | 0.500 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_660f33239428` | unsure | 0.500 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `c_49a8bc7bff82` | unsure | 0.500 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `c_bcd10553b235` | unsure | 0.500 | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `c_b8a6aaf2a99f` | ai | 0.500 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `c_8297cf3741ee` | unsure | 0.500 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `c_943899055a24` | unsure | 0.500 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_697d7dcf2383` | unsure | 0.500 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_7d987b87ec43` | unsure | 0.500 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_20739de53398` | unsure | 0.500 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_32cdc8653e18` | unsure | 0.500 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_bb4f652051b8` | unsure | 0.500 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

7 BROKE, 0 N/A, 49 HELD.
The new rejection is present in `logs/audit.jsonl`, for example:

```json
{"timestamp": "2026-11-15T08:17:00+00:00", "content_id": null, "creator_id": "attacker_MF02", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "text_too_short"}
```

This helped by eliminating three malformed-input paths that previously
reached scoring or crashed. It did not change valid submissions or address
the signal-one false-positive family; those remain the cost of keeping this
improvement narrowly scoped to input safety.

### Criterion Run Log — After Stretch Improvement

The post-change criterion run was produced by
`run_eval.py --label after_short` and saved in
`results/run_2026-11-15_0227_after_short.md`. Criteria 1, 2, 4, and 5 were
run three times; criterion 3 is carried over from its prior three-trial
appeal run because this stretch change does not affect appeals.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | At most 1 of 10 confirmed human pieces flagged `ai` | 4/10 flagged ai | 4/10 flagged ai | 4/10 flagged ai | MISS (unchanged) |
| 2. bad input | 400 for missing/empty/whitespace-only text and text over 50,000 characters, 5/5 each, never 500 | 20/20 returned 400, including the new short-input check | 20/20 returned 400, including the new short-input check | 20/20 returned 400, including the new short-input check | MET (unchanged; strengthened) |
| 3. appeal path | 5 of 5 appeals against valid content_ids change status to `under_review` and get logged | 5/5 under_review, 5/5 logged | 5/5 under_review, 5/5 logged | 5/5 under_review, 5/5 logged | MET (carried over) |
| 4. label coverage | All three `guess` values appear across 3 clearly-human/3 clearly-AI/4 borderline texts | only `ai` and `unsure` appeared | only `ai` and `unsure` appeared | only `ai` and `unsure` appeared | MISS (unchanged) |
| 5. correct side | At least 8 of 10 (5 human + 5 AI) get the correct side | 10/10 | 10/10 | 10/10 | MET (unchanged) |

The stretch change helped the bad-input axis without changing any verdict
for the model-scoring criteria: criterion 2 remained met, criteria 1 and 4
remained misses, and criterion 5 remained met.



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


## CAPSTONE

**The Shape**

I'm going with shape B, local with logs. I'm building a human review queue on top of the `/appeal` endpoint that already exists: a `GET /queue` so a reviewer can see what's waiting, and a `POST /resolve/<content_id>` so they can uphold or overturn the original call. It all lives in the same append-only audit log `/appeal` already writes to, nothing new to stand up. `RUNNING.md` has the one command that starts the service, checked against a clean checkout, plus what you need to have installed first: Python version, pinned dependencies, and the gpt2 model files, including their size. I'm also pasting in a real run of the service, logs and all, as proof it actually works and not just that the code reads fine.

**Out of scope**

I'm not measuring how long an appeal takes yet. That needs a timestamp on the resolution to measure against, and this round is what creates that timestamp, so it's the next thing to build, not this one.

I'm not touching either detection signal or how they're combined. This feature only reads and appends to the log; it doesn't rescore anything.

I'm not giving the queue a UI. `/queue` and `/resolve/<content_id>` are just routes, tested with curl like everything else here.


**How I Used AI**

**Moment 1**

**Moment 2**


**The Improvement**

**What I changed:**

**Which diagnosis pointed at it:**

**Attack Run — After**



**Run Log and Verdicts — After**



**Did it help, and how do I know:**



**What's Still Broken**



**Run Log and Verdicts**
