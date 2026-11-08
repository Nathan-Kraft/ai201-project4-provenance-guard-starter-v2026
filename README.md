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

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

**The numbers:**

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  | Our system's best guess is that this was written by a person, not generated by AI. |
| unsure |  | We can't confidently tell whether this was written by a person or by AI. |
| high-confidence AI |  | Our system's best guess is that this was generated by AI, not written by a person. |

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
  -d "{\"text\": \"The implementation of the proposed framework requires careful consideration of several key factors.\", \"creator_id\": \"nate\"}"
```

```json
{
  "confidence": 0.5,
  "content_id": "c_ca8c7c977e83",
  "guess": "unsure",
  "label": "Not built yet",
  "model_score": 0.5563,
  "style_score": null
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl.exe "http://127.0.0.1:5000/log?limit=5"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": null,
      "content_id": "c_723e06831389",
      "creator_id": "nate",
      "guess": null,
      "label": null,
      "model_score": 0.3046,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-11-08T07:22:47+00:00"
    },
    {
      "combined_score": null,
      "content_id": "c_ca8c7c977e83",
      "creator_id": "nate",
      "guess": "unsure",
      "label": null,
      "model_score": 0.5563,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-11-08T07:34:01+00:00"
    }
  ]
}
```

<!-- Note: the first entry above (c_723e06831389) was logged before the
     `guess` field was wired into the log_decision call, hence guess: null
     there vs "unsure" on the second. Both are real output from this
     session, pasted as-is. -->

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

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
