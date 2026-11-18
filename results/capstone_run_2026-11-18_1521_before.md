# Capstone run - before

- 3 trials per criterion
- 2026-11-18 15:21

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| queue membership |  | PASS | PASS | PASS |  |
| queue ordering |  | PASS | PASS | PASS |  |
| overturn replaces state |  | PASS | PASS | PASS |  |
| invalid corrected_guess |  | PASS | PASS | PASS |  |
| rejected resolve preserves status |  | PASS | PASS | PASS |  |

---

## What actually came back

The JSON below records the requests, responses, and checks for each trial.

### queue membership

**Trial 1**

```json
{
  "created_content_ids": [
    "c_07c4c691b774",
    "c_1c40d80afc4a",
    "c_410696038313",
    "c_0a6cfc32de45"
  ],
  "expected_under_review": [
    "c_07c4c691b774"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 19,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        }
      ]
    }
  },
  "observed_created_ids": [
    "c_07c4c691b774"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_07c4c691b774",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_07c4c691b774",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_1c40d80afc4a",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_1c40d80afc4a",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_1c40d80afc4a",
          "decision": "uphold",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_410696038313",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_410696038313",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_410696038313",
          "decision": "uphold",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_0a6cfc32de45",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      }
    }
  ]
}
```

**Trial 2**

```json
{
  "created_content_ids": [
    "c_c289907c5ba4",
    "c_3b81c28c5957",
    "c_061f3e160fc2",
    "c_91816b3db4de"
  ],
  "expected_under_review": [
    "c_c289907c5ba4"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 20,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        }
      ]
    }
  },
  "observed_created_ids": [
    "c_c289907c5ba4"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_c289907c5ba4",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_c289907c5ba4",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_3b81c28c5957",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_3b81c28c5957",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_3b81c28c5957",
          "decision": "uphold",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_061f3e160fc2",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_061f3e160fc2",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_061f3e160fc2",
          "decision": "uphold",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_91816b3db4de",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      }
    }
  ]
}
```

**Trial 3**

```json
{
  "created_content_ids": [
    "c_7727307f1a5e",
    "c_f04ee9cd7513",
    "c_1bda04e27315",
    "c_af193b62b938"
  ],
  "expected_under_review": [
    "c_7727307f1a5e"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 21,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_7727307f1a5e",
          "queued_since": "2026-11-18T21:21:05+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        }
      ]
    }
  },
  "observed_created_ids": [
    "c_7727307f1a5e"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_7727307f1a5e",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_7727307f1a5e",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_f04ee9cd7513",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_f04ee9cd7513",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_f04ee9cd7513",
          "decision": "uphold",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_1bda04e27315",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_1bda04e27315",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_1bda04e27315",
          "decision": "uphold",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_af193b62b938",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      }
    }
  ]
}
```

### queue ordering

**Trial 1**

```json
{
  "expected_order": [
    "c_90aec3050748",
    "c_14f7ef48f8dc",
    "c_204cd0ad283e"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 24,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_7727307f1a5e",
          "queued_since": "2026-11-18T21:21:05+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_90aec3050748",
          "queued_since": "2026-11-18T21:21:07+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_14f7ef48f8dc",
          "queued_since": "2026-11-18T21:21:08+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_204cd0ad283e",
          "queued_since": "2026-11-18T21:21:09+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        }
      ]
    }
  },
  "observed_order": [
    "c_90aec3050748",
    "c_14f7ef48f8dc",
    "c_204cd0ad283e"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_90aec3050748",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_90aec3050748",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_14f7ef48f8dc",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_14f7ef48f8dc",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_204cd0ad283e",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_204cd0ad283e",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    }
  ]
}
```

**Trial 2**

```json
{
  "expected_order": [
    "c_375ec3d200fb",
    "c_0ca51702ecae",
    "c_d0c6369801ac"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 27,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_7727307f1a5e",
          "queued_since": "2026-11-18T21:21:05+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_90aec3050748",
          "queued_since": "2026-11-18T21:21:07+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_14f7ef48f8dc",
          "queued_since": "2026-11-18T21:21:08+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_204cd0ad283e",
          "queued_since": "2026-11-18T21:21:09+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_375ec3d200fb",
          "queued_since": "2026-11-18T21:21:11+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_0ca51702ecae",
          "queued_since": "2026-11-18T21:21:12+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_d0c6369801ac",
          "queued_since": "2026-11-18T21:21:14+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        }
      ]
    }
  },
  "observed_order": [
    "c_375ec3d200fb",
    "c_0ca51702ecae",
    "c_d0c6369801ac"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_375ec3d200fb",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_375ec3d200fb",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_0ca51702ecae",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_0ca51702ecae",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_d0c6369801ac",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_d0c6369801ac",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    }
  ]
}
```

**Trial 3**

```json
{
  "expected_order": [
    "c_da661b829212",
    "c_4172555243fc",
    "c_e049ba150815"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 30,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_7727307f1a5e",
          "queued_since": "2026-11-18T21:21:05+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_90aec3050748",
          "queued_since": "2026-11-18T21:21:07+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_14f7ef48f8dc",
          "queued_since": "2026-11-18T21:21:08+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_204cd0ad283e",
          "queued_since": "2026-11-18T21:21:09+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_375ec3d200fb",
          "queued_since": "2026-11-18T21:21:11+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_0ca51702ecae",
          "queued_since": "2026-11-18T21:21:12+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_d0c6369801ac",
          "queued_since": "2026-11-18T21:21:14+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_da661b829212",
          "queued_since": "2026-11-18T21:21:16+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_4172555243fc",
          "queued_since": "2026-11-18T21:21:17+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_e049ba150815",
          "queued_since": "2026-11-18T21:21:18+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        }
      ]
    }
  },
  "observed_order": [
    "c_da661b829212",
    "c_4172555243fc",
    "c_e049ba150815"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_da661b829212",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_da661b829212",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_4172555243fc",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_4172555243fc",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_e049ba150815",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_e049ba150815",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      }
    }
  ]
}
```

### overturn replaces state

**Trial 1**

```json
{
  "checks": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_3a029fd4edf3",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "corrected_guess": "ai",
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_3a029fd4edf3",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_3a029fd4edf3",
          "decision": "overturn",
          "guess": "ai",
          "label": "Our system's best guess is that this was generated by AI, not written by a person.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      },
      "content": {
        "status": 200,
        "body": {
          "combined_score": null,
          "content_id": "c_3a029fd4edf3",
          "creator_id": null,
          "guess": "ai",
          "label": "Our system's best guess is that this was generated by AI, not written by a person.",
          "model_score": null,
          "status": "resolved",
          "style_score": null,
          "text": "This is a capstone evaluator submission with enough words for scoring."
        }
      },
      "matches": true
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_82a879e0d76a",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "corrected_guess": "human",
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_82a879e0d76a",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_82a879e0d76a",
          "decision": "overturn",
          "guess": "human",
          "label": "Our system's best guess is that this was written by a person, not generated by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      },
      "content": {
        "status": 200,
        "body": {
          "combined_score": null,
          "content_id": "c_82a879e0d76a",
          "creator_id": null,
          "guess": "human",
          "label": "Our system's best guess is that this was written by a person, not generated by AI.",
          "model_score": null,
          "status": "resolved",
          "style_score": null,
          "text": "This is a capstone evaluator submission with enough words for scoring."
        }
      },
      "matches": true
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_954c446db89e",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "corrected_guess": "unsure",
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_954c446db89e",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_954c446db89e",
          "decision": "overturn",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      },
      "content": {
        "status": 200,
        "body": {
          "combined_score": null,
          "content_id": "c_954c446db89e",
          "creator_id": null,
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": null,
          "status": "resolved",
          "style_score": null,
          "text": "This is a capstone evaluator submission with enough words for scoring."
        }
      },
      "matches": true
    }
  ],
  "passed": true
}
```

**Trial 2**

```json
{
  "checks": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_b57f1a85095d",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "corrected_guess": "ai",
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_b57f1a85095d",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_b57f1a85095d",
          "decision": "overturn",
          "guess": "ai",
          "label": "Our system's best guess is that this was generated by AI, not written by a person.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      },
      "content": {
        "status": 200,
        "body": {
          "combined_score": null,
          "content_id": "c_b57f1a85095d",
          "creator_id": null,
          "guess": "ai",
          "label": "Our system's best guess is that this was generated by AI, not written by a person.",
          "model_score": null,
          "status": "resolved",
          "style_score": null,
          "text": "This is a capstone evaluator submission with enough words for scoring."
        }
      },
      "matches": true
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_35051306111a",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "corrected_guess": "human",
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_35051306111a",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_35051306111a",
          "decision": "overturn",
          "guess": "human",
          "label": "Our system's best guess is that this was written by a person, not generated by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      },
      "content": {
        "status": 200,
        "body": {
          "combined_score": null,
          "content_id": "c_35051306111a",
          "creator_id": null,
          "guess": "human",
          "label": "Our system's best guess is that this was written by a person, not generated by AI.",
          "model_score": null,
          "status": "resolved",
          "style_score": null,
          "text": "This is a capstone evaluator submission with enough words for scoring."
        }
      },
      "matches": true
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_5266134becac",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "corrected_guess": "unsure",
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_5266134becac",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_5266134becac",
          "decision": "overturn",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      },
      "content": {
        "status": 200,
        "body": {
          "combined_score": null,
          "content_id": "c_5266134becac",
          "creator_id": null,
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": null,
          "status": "resolved",
          "style_score": null,
          "text": "This is a capstone evaluator submission with enough words for scoring."
        }
      },
      "matches": true
    }
  ],
  "passed": true
}
```

**Trial 3**

```json
{
  "checks": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_c321b87e9ebf",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "corrected_guess": "ai",
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_c321b87e9ebf",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_c321b87e9ebf",
          "decision": "overturn",
          "guess": "ai",
          "label": "Our system's best guess is that this was generated by AI, not written by a person.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      },
      "content": {
        "status": 200,
        "body": {
          "combined_score": null,
          "content_id": "c_c321b87e9ebf",
          "creator_id": null,
          "guess": "ai",
          "label": "Our system's best guess is that this was generated by AI, not written by a person.",
          "model_score": null,
          "status": "resolved",
          "style_score": null,
          "text": "This is a capstone evaluator submission with enough words for scoring."
        }
      },
      "matches": true
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_1b3a487d3f37",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "corrected_guess": "human",
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_1b3a487d3f37",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_1b3a487d3f37",
          "decision": "overturn",
          "guess": "human",
          "label": "Our system's best guess is that this was written by a person, not generated by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      },
      "content": {
        "status": 200,
        "body": {
          "combined_score": null,
          "content_id": "c_1b3a487d3f37",
          "creator_id": null,
          "guess": "human",
          "label": "Our system's best guess is that this was written by a person, not generated by AI.",
          "model_score": null,
          "status": "resolved",
          "style_score": null,
          "text": "This is a capstone evaluator submission with enough words for scoring."
        }
      },
      "matches": true
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_0ea9550d2a5e",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "corrected_guess": "unsure",
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_0ea9550d2a5e",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_0ea9550d2a5e",
          "decision": "overturn",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "message": "Resolution recorded.",
          "status": "resolved"
        }
      },
      "content": {
        "status": 200,
        "body": {
          "combined_score": null,
          "content_id": "c_0ea9550d2a5e",
          "creator_id": null,
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": null,
          "status": "resolved",
          "style_score": null,
          "text": "This is a capstone evaluator submission with enough words for scoring."
        }
      },
      "matches": true
    }
  ],
  "passed": true
}
```

### invalid corrected_guess

**Trial 1**

```json
{
  "submit": {
    "status": 200,
    "body": {
      "confidence": 0.5,
      "content_id": "c_19cdb46d3378",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "style_score": 0.6666666666666666
    }
  },
  "corrected_guess": "banana",
  "appeal": {
    "status": 200,
    "body": {
      "content_id": "c_19cdb46d3378",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_19cdb46d3378",
      "creator_id": "capstone_invalid_guess_1",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "resolve": {
    "status": 400,
    "body": {
      "error": "bad_request",
      "message": "Overturning requires \"corrected_guess\" to be one of \"ai\", \"human\", or \"unsure\"."
    }
  },
  "after": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_19cdb46d3378",
      "creator_id": "capstone_invalid_guess_1",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "queue": {
    "status": 200,
    "body": {
      "count": 31,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_7727307f1a5e",
          "queued_since": "2026-11-18T21:21:05+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_90aec3050748",
          "queued_since": "2026-11-18T21:21:07+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_14f7ef48f8dc",
          "queued_since": "2026-11-18T21:21:08+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_204cd0ad283e",
          "queued_since": "2026-11-18T21:21:09+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_375ec3d200fb",
          "queued_since": "2026-11-18T21:21:11+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_0ca51702ecae",
          "queued_since": "2026-11-18T21:21:12+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_d0c6369801ac",
          "queued_since": "2026-11-18T21:21:14+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_da661b829212",
          "queued_since": "2026-11-18T21:21:16+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_4172555243fc",
          "queued_since": "2026-11-18T21:21:17+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_e049ba150815",
          "queued_since": "2026-11-18T21:21:18+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_19cdb46d3378",
          "queued_since": "2026-11-18T21:21:21+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        }
      ]
    }
  },
  "passed": true
}
```

**Trial 2**

```json
{
  "submit": {
    "status": 200,
    "body": {
      "confidence": 0.5,
      "content_id": "c_6d358c779170",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "style_score": 0.6666666666666666
    }
  },
  "corrected_guess": "banana",
  "appeal": {
    "status": 200,
    "body": {
      "content_id": "c_6d358c779170",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_6d358c779170",
      "creator_id": "capstone_invalid_guess_2",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "resolve": {
    "status": 400,
    "body": {
      "error": "bad_request",
      "message": "Overturning requires \"corrected_guess\" to be one of \"ai\", \"human\", or \"unsure\"."
    }
  },
  "after": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_6d358c779170",
      "creator_id": "capstone_invalid_guess_2",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "queue": {
    "status": 200,
    "body": {
      "count": 32,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_7727307f1a5e",
          "queued_since": "2026-11-18T21:21:05+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_90aec3050748",
          "queued_since": "2026-11-18T21:21:07+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_14f7ef48f8dc",
          "queued_since": "2026-11-18T21:21:08+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_204cd0ad283e",
          "queued_since": "2026-11-18T21:21:09+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_375ec3d200fb",
          "queued_since": "2026-11-18T21:21:11+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_0ca51702ecae",
          "queued_since": "2026-11-18T21:21:12+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_d0c6369801ac",
          "queued_since": "2026-11-18T21:21:14+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_da661b829212",
          "queued_since": "2026-11-18T21:21:16+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_4172555243fc",
          "queued_since": "2026-11-18T21:21:17+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_e049ba150815",
          "queued_since": "2026-11-18T21:21:18+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_19cdb46d3378",
          "queued_since": "2026-11-18T21:21:21+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_6d358c779170",
          "queued_since": "2026-11-18T21:21:23+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        }
      ]
    }
  },
  "passed": true
}
```

**Trial 3**

```json
{
  "submit": {
    "status": 200,
    "body": {
      "confidence": 0.5,
      "content_id": "c_9e62e1f78e5b",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "style_score": 0.6666666666666666
    }
  },
  "corrected_guess": "banana",
  "appeal": {
    "status": 200,
    "body": {
      "content_id": "c_9e62e1f78e5b",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_9e62e1f78e5b",
      "creator_id": "capstone_invalid_guess_3",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "resolve": {
    "status": 400,
    "body": {
      "error": "bad_request",
      "message": "Overturning requires \"corrected_guess\" to be one of \"ai\", \"human\", or \"unsure\"."
    }
  },
  "after": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_9e62e1f78e5b",
      "creator_id": "capstone_invalid_guess_3",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "queue": {
    "status": 200,
    "body": {
      "count": 33,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_7727307f1a5e",
          "queued_since": "2026-11-18T21:21:05+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_90aec3050748",
          "queued_since": "2026-11-18T21:21:07+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_14f7ef48f8dc",
          "queued_since": "2026-11-18T21:21:08+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_204cd0ad283e",
          "queued_since": "2026-11-18T21:21:09+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_375ec3d200fb",
          "queued_since": "2026-11-18T21:21:11+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_0ca51702ecae",
          "queued_since": "2026-11-18T21:21:12+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_d0c6369801ac",
          "queued_since": "2026-11-18T21:21:14+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_da661b829212",
          "queued_since": "2026-11-18T21:21:16+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_4172555243fc",
          "queued_since": "2026-11-18T21:21:17+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_e049ba150815",
          "queued_since": "2026-11-18T21:21:18+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_19cdb46d3378",
          "queued_since": "2026-11-18T21:21:21+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_6d358c779170",
          "queued_since": "2026-11-18T21:21:23+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_9e62e1f78e5b",
          "queued_since": "2026-11-18T21:21:25+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        }
      ]
    }
  },
  "passed": true
}
```

### rejected resolve preserves status

**Trial 1**

```json
{
  "submit": {
    "status": 200,
    "body": {
      "confidence": 0.5,
      "content_id": "c_19de52aeb078",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "style_score": 0.6666666666666666
    }
  },
  "appeal": {
    "status": 200,
    "body": {
      "content_id": "c_19de52aeb078",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_19de52aeb078",
      "creator_id": "capstone_rejected_resolve_1",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "resolve": {
    "status": 400,
    "body": {
      "error": "bad_request",
      "message": "Send JSON with \"decision\" set to \"uphold\" or \"overturn\"."
    }
  },
  "after": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_19de52aeb078",
      "creator_id": "capstone_rejected_resolve_1",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "queue": {
    "status": 200,
    "body": {
      "count": 34,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_7727307f1a5e",
          "queued_since": "2026-11-18T21:21:05+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_90aec3050748",
          "queued_since": "2026-11-18T21:21:07+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_14f7ef48f8dc",
          "queued_since": "2026-11-18T21:21:08+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_204cd0ad283e",
          "queued_since": "2026-11-18T21:21:09+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_375ec3d200fb",
          "queued_since": "2026-11-18T21:21:11+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_0ca51702ecae",
          "queued_since": "2026-11-18T21:21:12+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_d0c6369801ac",
          "queued_since": "2026-11-18T21:21:14+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_da661b829212",
          "queued_since": "2026-11-18T21:21:16+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_4172555243fc",
          "queued_since": "2026-11-18T21:21:17+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_e049ba150815",
          "queued_since": "2026-11-18T21:21:18+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_19cdb46d3378",
          "queued_since": "2026-11-18T21:21:21+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_6d358c779170",
          "queued_since": "2026-11-18T21:21:23+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_9e62e1f78e5b",
          "queued_since": "2026-11-18T21:21:25+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_19de52aeb078",
          "queued_since": "2026-11-18T21:21:27+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        }
      ]
    }
  },
  "passed": true
}
```

**Trial 2**

```json
{
  "submit": {
    "status": 200,
    "body": {
      "confidence": 0.5,
      "content_id": "c_362586a69ff0",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "style_score": 0.6666666666666666
    }
  },
  "appeal": {
    "status": 200,
    "body": {
      "content_id": "c_362586a69ff0",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_362586a69ff0",
      "creator_id": "capstone_rejected_resolve_2",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "resolve": {
    "status": 400,
    "body": {
      "error": "bad_request",
      "message": "Send JSON with \"decision\" set to \"uphold\" or \"overturn\"."
    }
  },
  "after": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_362586a69ff0",
      "creator_id": "capstone_rejected_resolve_2",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "queue": {
    "status": 200,
    "body": {
      "count": 35,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_7727307f1a5e",
          "queued_since": "2026-11-18T21:21:05+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_90aec3050748",
          "queued_since": "2026-11-18T21:21:07+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_14f7ef48f8dc",
          "queued_since": "2026-11-18T21:21:08+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_204cd0ad283e",
          "queued_since": "2026-11-18T21:21:09+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_375ec3d200fb",
          "queued_since": "2026-11-18T21:21:11+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_0ca51702ecae",
          "queued_since": "2026-11-18T21:21:12+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_d0c6369801ac",
          "queued_since": "2026-11-18T21:21:14+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_da661b829212",
          "queued_since": "2026-11-18T21:21:16+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_4172555243fc",
          "queued_since": "2026-11-18T21:21:17+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_e049ba150815",
          "queued_since": "2026-11-18T21:21:18+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_19cdb46d3378",
          "queued_since": "2026-11-18T21:21:21+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_6d358c779170",
          "queued_since": "2026-11-18T21:21:23+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_9e62e1f78e5b",
          "queued_since": "2026-11-18T21:21:25+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_19de52aeb078",
          "queued_since": "2026-11-18T21:21:27+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_362586a69ff0",
          "queued_since": "2026-11-18T21:21:29+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        }
      ]
    }
  },
  "passed": true
}
```

**Trial 3**

```json
{
  "submit": {
    "status": 200,
    "body": {
      "confidence": 0.5,
      "content_id": "c_da49fc00e3d0",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "style_score": 0.6666666666666666
    }
  },
  "appeal": {
    "status": 200,
    "body": {
      "content_id": "c_da49fc00e3d0",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_da49fc00e3d0",
      "creator_id": "capstone_rejected_resolve_3",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "resolve": {
    "status": 400,
    "body": {
      "error": "bad_request",
      "message": "Send JSON with \"decision\" set to \"uphold\" or \"overturn\"."
    }
  },
  "after": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_da49fc00e3d0",
      "creator_id": "capstone_rejected_resolve_3",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "status": "under_review",
      "style_score": 0.6666666666666666,
      "text": "This is a capstone evaluator submission with enough words for scoring."
    }
  },
  "queue": {
    "status": 200,
    "body": {
      "count": 36,
      "queue": [
        {
          "content_id": "c_278f71897e36",
          "queued_since": "2026-11-18T20:47:27+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_b3c06ab0d5ed",
          "queued_since": "2026-11-18T20:47:28+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_8e7e74445bc9",
          "queued_since": "2026-11-18T20:47:30+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_de4d71629159",
          "queued_since": "2026-11-18T20:47:32+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_1d6070c7ef1f",
          "queued_since": "2026-11-18T20:47:33+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_1879c8305a83",
          "queued_since": "2026-11-18T20:47:34+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_5aff9cbc6302",
          "queued_since": "2026-11-18T20:47:36+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_e035c813cddf",
          "queued_since": "2026-11-18T20:47:37+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_791141b7357a",
          "queued_since": "2026-11-18T20:47:38+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_1e03a5fdec6b",
          "queued_since": "2026-11-18T20:47:40+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_5e69a1264a23",
          "queued_since": "2026-11-18T20:47:41+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_0039887144b2",
          "queued_since": "2026-11-18T20:47:42+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_044329ae8cf0",
          "queued_since": "2026-11-18T20:47:45+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_ebd889ea0b7f",
          "queued_since": "2026-11-18T20:47:46+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_2f4c4c9b8e88",
          "queued_since": "2026-11-18T20:47:48+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_9bdbc4fc542c",
          "queued_since": "2026-11-18T20:47:50+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_609f8d6c1009",
          "queued_since": "2026-11-18T20:47:52+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_672853a687f3",
          "queued_since": "2026-11-18T20:47:53+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        },
        {
          "content_id": "c_07c4c691b774",
          "queued_since": "2026-11-18T21:21:01+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_c289907c5ba4",
          "queued_since": "2026-11-18T21:21:03+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_7727307f1a5e",
          "queued_since": "2026-11-18T21:21:05+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_90aec3050748",
          "queued_since": "2026-11-18T21:21:07+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_14f7ef48f8dc",
          "queued_since": "2026-11-18T21:21:08+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_204cd0ad283e",
          "queued_since": "2026-11-18T21:21:09+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_375ec3d200fb",
          "queued_since": "2026-11-18T21:21:11+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_0ca51702ecae",
          "queued_since": "2026-11-18T21:21:12+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_d0c6369801ac",
          "queued_since": "2026-11-18T21:21:14+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_da661b829212",
          "queued_since": "2026-11-18T21:21:16+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_4172555243fc",
          "queued_since": "2026-11-18T21:21:17+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_e049ba150815",
          "queued_since": "2026-11-18T21:21:18+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_19cdb46d3378",
          "queued_since": "2026-11-18T21:21:21+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_6d358c779170",
          "queued_since": "2026-11-18T21:21:23+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_9e62e1f78e5b",
          "queued_since": "2026-11-18T21:21:25+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_19de52aeb078",
          "queued_since": "2026-11-18T21:21:27+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_362586a69ff0",
          "queued_since": "2026-11-18T21:21:29+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_da49fc00e3d0",
          "queued_since": "2026-11-18T21:21:31+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        }
      ]
    }
  },
  "passed": true
}
```
