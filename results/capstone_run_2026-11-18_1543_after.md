# Capstone run - after

- 3 trials per criterion
- 2026-11-18 15:43

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
    "c_fdce6b3af0bc",
    "c_0df89644257d",
    "c_bd82699d8560",
    "c_766b5191b835"
  ],
  "expected_under_review": [
    "c_fdce6b3af0bc"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 37,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        }
      ]
    }
  },
  "observed_created_ids": [
    "c_fdce6b3af0bc"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_fdce6b3af0bc",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_fdce6b3af0bc",
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
          "content_id": "c_0df89644257d",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_0df89644257d",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_0df89644257d",
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
          "content_id": "c_bd82699d8560",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_bd82699d8560",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_bd82699d8560",
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
          "content_id": "c_766b5191b835",
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
    "c_4e79b90da243",
    "c_e3903a013783",
    "c_936728bcf21c",
    "c_b0a5324a3c4a"
  ],
  "expected_under_review": [
    "c_4e79b90da243"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 38,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        }
      ]
    }
  },
  "observed_created_ids": [
    "c_4e79b90da243"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_4e79b90da243",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_4e79b90da243",
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
          "content_id": "c_e3903a013783",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_e3903a013783",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_e3903a013783",
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
          "content_id": "c_936728bcf21c",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_936728bcf21c",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_936728bcf21c",
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
          "content_id": "c_b0a5324a3c4a",
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
    "c_5fdf3e9a3ff0",
    "c_458ebe0295ad",
    "c_4d09aeaf7c73",
    "c_6c93a0621a8c"
  ],
  "expected_under_review": [
    "c_5fdf3e9a3ff0"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 39,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_5fdf3e9a3ff0",
          "queued_since": "2026-11-18T21:43:07+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        }
      ]
    }
  },
  "observed_created_ids": [
    "c_5fdf3e9a3ff0"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_5fdf3e9a3ff0",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_5fdf3e9a3ff0",
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
          "content_id": "c_458ebe0295ad",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_458ebe0295ad",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_458ebe0295ad",
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
          "content_id": "c_4d09aeaf7c73",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_4d09aeaf7c73",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_4d09aeaf7c73",
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
          "content_id": "c_6c93a0621a8c",
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
    "c_f9caee03f5b8",
    "c_b9f23d528a89",
    "c_49718701cc2f"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 42,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_5fdf3e9a3ff0",
          "queued_since": "2026-11-18T21:43:07+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_f9caee03f5b8",
          "queued_since": "2026-11-18T21:43:09+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_b9f23d528a89",
          "queued_since": "2026-11-18T21:43:10+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_49718701cc2f",
          "queued_since": "2026-11-18T21:43:12+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        }
      ]
    }
  },
  "observed_order": [
    "c_f9caee03f5b8",
    "c_b9f23d528a89",
    "c_49718701cc2f"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_f9caee03f5b8",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_f9caee03f5b8",
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
          "content_id": "c_b9f23d528a89",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_b9f23d528a89",
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
          "content_id": "c_49718701cc2f",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_49718701cc2f",
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
    "c_8d741efd87a6",
    "c_1e7bc1dc13ba",
    "c_798e54194785"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 45,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_5fdf3e9a3ff0",
          "queued_since": "2026-11-18T21:43:07+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_f9caee03f5b8",
          "queued_since": "2026-11-18T21:43:09+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_b9f23d528a89",
          "queued_since": "2026-11-18T21:43:10+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_49718701cc2f",
          "queued_since": "2026-11-18T21:43:12+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_8d741efd87a6",
          "queued_since": "2026-11-18T21:43:14+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_1e7bc1dc13ba",
          "queued_since": "2026-11-18T21:43:15+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_798e54194785",
          "queued_since": "2026-11-18T21:43:16+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        }
      ]
    }
  },
  "observed_order": [
    "c_8d741efd87a6",
    "c_1e7bc1dc13ba",
    "c_798e54194785"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_8d741efd87a6",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_8d741efd87a6",
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
          "content_id": "c_1e7bc1dc13ba",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_1e7bc1dc13ba",
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
          "content_id": "c_798e54194785",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_798e54194785",
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
    "c_2666dafd9a22",
    "c_a627d2811454",
    "c_48df2bf2044b"
  ],
  "queue": {
    "status": 200,
    "body": {
      "count": 48,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_5fdf3e9a3ff0",
          "queued_since": "2026-11-18T21:43:07+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_f9caee03f5b8",
          "queued_since": "2026-11-18T21:43:09+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_b9f23d528a89",
          "queued_since": "2026-11-18T21:43:10+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_49718701cc2f",
          "queued_since": "2026-11-18T21:43:12+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_8d741efd87a6",
          "queued_since": "2026-11-18T21:43:14+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_1e7bc1dc13ba",
          "queued_since": "2026-11-18T21:43:15+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_798e54194785",
          "queued_since": "2026-11-18T21:43:16+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_2666dafd9a22",
          "queued_since": "2026-11-18T21:43:18+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_a627d2811454",
          "queued_since": "2026-11-18T21:43:20+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_48df2bf2044b",
          "queued_since": "2026-11-18T21:43:21+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        }
      ]
    }
  },
  "observed_order": [
    "c_2666dafd9a22",
    "c_a627d2811454",
    "c_48df2bf2044b"
  ],
  "passed": true,
  "setup": [
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_2666dafd9a22",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_2666dafd9a22",
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
          "content_id": "c_a627d2811454",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_a627d2811454",
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
          "content_id": "c_48df2bf2044b",
          "guess": "unsure",
          "label": "We can't confidently tell whether this was written by a person or by AI.",
          "model_score": 0.0753,
          "style_score": 0.6666666666666666
        }
      },
      "appeal": {
        "status": 200,
        "body": {
          "content_id": "c_48df2bf2044b",
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
          "content_id": "c_406db2b66b45",
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
          "content_id": "c_406db2b66b45",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_406db2b66b45",
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
          "content_id": "c_406db2b66b45",
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
          "content_id": "c_aa4bb946db1f",
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
          "content_id": "c_aa4bb946db1f",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_aa4bb946db1f",
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
          "content_id": "c_aa4bb946db1f",
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
          "content_id": "c_e1fd13d52ae2",
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
          "content_id": "c_e1fd13d52ae2",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_e1fd13d52ae2",
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
          "content_id": "c_e1fd13d52ae2",
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
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_d37b2e01a3b6",
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
          "content_id": "c_d37b2e01a3b6",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_d37b2e01a3b6",
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
          "content_id": "c_d37b2e01a3b6",
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
          "content_id": "c_31f6bb0a90f0",
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
          "content_id": "c_31f6bb0a90f0",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_31f6bb0a90f0",
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
          "content_id": "c_31f6bb0a90f0",
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
          "content_id": "c_c40ed89ca142",
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
          "content_id": "c_c40ed89ca142",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_c40ed89ca142",
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
          "content_id": "c_c40ed89ca142",
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
          "content_id": "c_92d6bfea47fc",
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
          "content_id": "c_92d6bfea47fc",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_92d6bfea47fc",
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
          "content_id": "c_92d6bfea47fc",
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
          "content_id": "c_35a9770ef792",
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
          "content_id": "c_35a9770ef792",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_35a9770ef792",
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
          "content_id": "c_35a9770ef792",
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
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_5886cf1f2e65",
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
          "content_id": "c_5886cf1f2e65",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_5886cf1f2e65",
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
          "content_id": "c_5886cf1f2e65",
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
          "content_id": "c_cef650ec1ea9",
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
          "content_id": "c_cef650ec1ea9",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_cef650ec1ea9",
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
          "content_id": "c_cef650ec1ea9",
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
          "content_id": "c_5650f54c14b5",
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
          "content_id": "c_5650f54c14b5",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_5650f54c14b5",
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
          "content_id": "c_5650f54c14b5",
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
          "content_id": "c_d42b5b05530e",
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
          "content_id": "c_d42b5b05530e",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_d42b5b05530e",
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
          "content_id": "c_d42b5b05530e",
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
          "content_id": "c_b2b0ecc17132",
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
          "content_id": "c_b2b0ecc17132",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_b2b0ecc17132",
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
          "content_id": "c_b2b0ecc17132",
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
    },
    {
      "submit": {
        "status": 200,
        "body": {
          "confidence": 0.5,
          "content_id": "c_9f3fc9eb6cd9",
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
          "content_id": "c_9f3fc9eb6cd9",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_9f3fc9eb6cd9",
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
          "content_id": "c_9f3fc9eb6cd9",
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
          "content_id": "c_01742014fd6e",
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
          "content_id": "c_01742014fd6e",
          "message": "Your appeal has been recorded. A person will review this submission.",
          "status": "under_review"
        }
      },
      "resolve": {
        "status": 200,
        "body": {
          "content_id": "c_01742014fd6e",
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
          "content_id": "c_01742014fd6e",
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
      "content_id": "c_eee5bc8b1965",
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
      "content_id": "c_eee5bc8b1965",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_eee5bc8b1965",
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
      "content_id": "c_eee5bc8b1965",
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
      "count": 49,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_5fdf3e9a3ff0",
          "queued_since": "2026-11-18T21:43:07+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_f9caee03f5b8",
          "queued_since": "2026-11-18T21:43:09+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_b9f23d528a89",
          "queued_since": "2026-11-18T21:43:10+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_49718701cc2f",
          "queued_since": "2026-11-18T21:43:12+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_8d741efd87a6",
          "queued_since": "2026-11-18T21:43:14+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_1e7bc1dc13ba",
          "queued_since": "2026-11-18T21:43:15+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_798e54194785",
          "queued_since": "2026-11-18T21:43:16+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_2666dafd9a22",
          "queued_since": "2026-11-18T21:43:18+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_a627d2811454",
          "queued_since": "2026-11-18T21:43:20+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_48df2bf2044b",
          "queued_since": "2026-11-18T21:43:21+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_eee5bc8b1965",
          "queued_since": "2026-11-18T21:43:25+00:00",
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
      "content_id": "c_03333a17bd21",
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
      "content_id": "c_03333a17bd21",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_03333a17bd21",
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
      "content_id": "c_03333a17bd21",
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
      "count": 50,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_5fdf3e9a3ff0",
          "queued_since": "2026-11-18T21:43:07+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_f9caee03f5b8",
          "queued_since": "2026-11-18T21:43:09+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_b9f23d528a89",
          "queued_since": "2026-11-18T21:43:10+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_49718701cc2f",
          "queued_since": "2026-11-18T21:43:12+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_8d741efd87a6",
          "queued_since": "2026-11-18T21:43:14+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_1e7bc1dc13ba",
          "queued_since": "2026-11-18T21:43:15+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_798e54194785",
          "queued_since": "2026-11-18T21:43:16+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_2666dafd9a22",
          "queued_since": "2026-11-18T21:43:18+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_a627d2811454",
          "queued_since": "2026-11-18T21:43:20+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_48df2bf2044b",
          "queued_since": "2026-11-18T21:43:21+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_eee5bc8b1965",
          "queued_since": "2026-11-18T21:43:25+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_03333a17bd21",
          "queued_since": "2026-11-18T21:43:27+00:00",
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
      "content_id": "c_0978249d83bc",
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
      "content_id": "c_0978249d83bc",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_0978249d83bc",
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
      "content_id": "c_0978249d83bc",
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
      "count": 51,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_5fdf3e9a3ff0",
          "queued_since": "2026-11-18T21:43:07+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_f9caee03f5b8",
          "queued_since": "2026-11-18T21:43:09+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_b9f23d528a89",
          "queued_since": "2026-11-18T21:43:10+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_49718701cc2f",
          "queued_since": "2026-11-18T21:43:12+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_8d741efd87a6",
          "queued_since": "2026-11-18T21:43:14+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_1e7bc1dc13ba",
          "queued_since": "2026-11-18T21:43:15+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_798e54194785",
          "queued_since": "2026-11-18T21:43:16+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_2666dafd9a22",
          "queued_since": "2026-11-18T21:43:18+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_a627d2811454",
          "queued_since": "2026-11-18T21:43:20+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_48df2bf2044b",
          "queued_since": "2026-11-18T21:43:21+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_eee5bc8b1965",
          "queued_since": "2026-11-18T21:43:25+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_03333a17bd21",
          "queued_since": "2026-11-18T21:43:27+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_0978249d83bc",
          "queued_since": "2026-11-18T21:43:29+00:00",
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
      "content_id": "c_77fd86e5d0e1",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "style_score": 0.6666666666666666
    }
  },
  "appeal": {
    "status": 200,
    "body": {
      "content_id": "c_77fd86e5d0e1",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_77fd86e5d0e1",
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
      "content_id": "c_77fd86e5d0e1",
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
      "count": 52,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_5fdf3e9a3ff0",
          "queued_since": "2026-11-18T21:43:07+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_f9caee03f5b8",
          "queued_since": "2026-11-18T21:43:09+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_b9f23d528a89",
          "queued_since": "2026-11-18T21:43:10+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_49718701cc2f",
          "queued_since": "2026-11-18T21:43:12+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_8d741efd87a6",
          "queued_since": "2026-11-18T21:43:14+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_1e7bc1dc13ba",
          "queued_since": "2026-11-18T21:43:15+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_798e54194785",
          "queued_since": "2026-11-18T21:43:16+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_2666dafd9a22",
          "queued_since": "2026-11-18T21:43:18+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_a627d2811454",
          "queued_since": "2026-11-18T21:43:20+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_48df2bf2044b",
          "queued_since": "2026-11-18T21:43:21+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_eee5bc8b1965",
          "queued_since": "2026-11-18T21:43:25+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_03333a17bd21",
          "queued_since": "2026-11-18T21:43:27+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_0978249d83bc",
          "queued_since": "2026-11-18T21:43:29+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_77fd86e5d0e1",
          "queued_since": "2026-11-18T21:43:32+00:00",
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
      "content_id": "c_36d05256a96d",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "style_score": 0.6666666666666666
    }
  },
  "appeal": {
    "status": 200,
    "body": {
      "content_id": "c_36d05256a96d",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_36d05256a96d",
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
      "content_id": "c_36d05256a96d",
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
      "count": 53,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_5fdf3e9a3ff0",
          "queued_since": "2026-11-18T21:43:07+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_f9caee03f5b8",
          "queued_since": "2026-11-18T21:43:09+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_b9f23d528a89",
          "queued_since": "2026-11-18T21:43:10+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_49718701cc2f",
          "queued_since": "2026-11-18T21:43:12+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_8d741efd87a6",
          "queued_since": "2026-11-18T21:43:14+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_1e7bc1dc13ba",
          "queued_since": "2026-11-18T21:43:15+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_798e54194785",
          "queued_since": "2026-11-18T21:43:16+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_2666dafd9a22",
          "queued_since": "2026-11-18T21:43:18+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_a627d2811454",
          "queued_since": "2026-11-18T21:43:20+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_48df2bf2044b",
          "queued_since": "2026-11-18T21:43:21+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_eee5bc8b1965",
          "queued_since": "2026-11-18T21:43:25+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_03333a17bd21",
          "queued_since": "2026-11-18T21:43:27+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_0978249d83bc",
          "queued_since": "2026-11-18T21:43:29+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_77fd86e5d0e1",
          "queued_since": "2026-11-18T21:43:32+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_36d05256a96d",
          "queued_since": "2026-11-18T21:43:36+00:00",
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
      "content_id": "c_381fd8a0779b",
      "guess": "unsure",
      "label": "We can't confidently tell whether this was written by a person or by AI.",
      "model_score": 0.0753,
      "style_score": 0.6666666666666666
    }
  },
  "appeal": {
    "status": 200,
    "body": {
      "content_id": "c_381fd8a0779b",
      "message": "Your appeal has been recorded. A person will review this submission.",
      "status": "under_review"
    }
  },
  "before": {
    "status": 200,
    "body": {
      "combined_score": 0.5,
      "content_id": "c_381fd8a0779b",
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
      "content_id": "c_381fd8a0779b",
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
      "count": 54,
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
        },
        {
          "content_id": "c_fdce6b3af0bc",
          "queued_since": "2026-11-18T21:43:02+00:00",
          "reasoning": "Capstone appeal membership_1_under_review_0."
        },
        {
          "content_id": "c_4e79b90da243",
          "queued_since": "2026-11-18T21:43:05+00:00",
          "reasoning": "Capstone appeal membership_2_under_review_0."
        },
        {
          "content_id": "c_5fdf3e9a3ff0",
          "queued_since": "2026-11-18T21:43:07+00:00",
          "reasoning": "Capstone appeal membership_3_under_review_0."
        },
        {
          "content_id": "c_f9caee03f5b8",
          "queued_since": "2026-11-18T21:43:09+00:00",
          "reasoning": "Capstone appeal ordering_1_0."
        },
        {
          "content_id": "c_b9f23d528a89",
          "queued_since": "2026-11-18T21:43:10+00:00",
          "reasoning": "Capstone appeal ordering_1_1."
        },
        {
          "content_id": "c_49718701cc2f",
          "queued_since": "2026-11-18T21:43:12+00:00",
          "reasoning": "Capstone appeal ordering_1_2."
        },
        {
          "content_id": "c_8d741efd87a6",
          "queued_since": "2026-11-18T21:43:14+00:00",
          "reasoning": "Capstone appeal ordering_2_0."
        },
        {
          "content_id": "c_1e7bc1dc13ba",
          "queued_since": "2026-11-18T21:43:15+00:00",
          "reasoning": "Capstone appeal ordering_2_1."
        },
        {
          "content_id": "c_798e54194785",
          "queued_since": "2026-11-18T21:43:16+00:00",
          "reasoning": "Capstone appeal ordering_2_2."
        },
        {
          "content_id": "c_2666dafd9a22",
          "queued_since": "2026-11-18T21:43:18+00:00",
          "reasoning": "Capstone appeal ordering_3_0."
        },
        {
          "content_id": "c_a627d2811454",
          "queued_since": "2026-11-18T21:43:20+00:00",
          "reasoning": "Capstone appeal ordering_3_1."
        },
        {
          "content_id": "c_48df2bf2044b",
          "queued_since": "2026-11-18T21:43:21+00:00",
          "reasoning": "Capstone appeal ordering_3_2."
        },
        {
          "content_id": "c_eee5bc8b1965",
          "queued_since": "2026-11-18T21:43:25+00:00",
          "reasoning": "Capstone appeal invalid_guess_1."
        },
        {
          "content_id": "c_03333a17bd21",
          "queued_since": "2026-11-18T21:43:27+00:00",
          "reasoning": "Capstone appeal invalid_guess_2."
        },
        {
          "content_id": "c_0978249d83bc",
          "queued_since": "2026-11-18T21:43:29+00:00",
          "reasoning": "Capstone appeal invalid_guess_3."
        },
        {
          "content_id": "c_77fd86e5d0e1",
          "queued_since": "2026-11-18T21:43:32+00:00",
          "reasoning": "Capstone appeal rejected_resolve_1."
        },
        {
          "content_id": "c_36d05256a96d",
          "queued_since": "2026-11-18T21:43:36+00:00",
          "reasoning": "Capstone appeal rejected_resolve_2."
        },
        {
          "content_id": "c_381fd8a0779b",
          "queued_since": "2026-11-18T21:43:39+00:00",
          "reasoning": "Capstone appeal rejected_resolve_3."
        }
      ]
    }
  },
  "passed": true
}
```
