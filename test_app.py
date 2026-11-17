#!/usr/bin/env python3
"""
Route-level tests for the human review queue behind /appeal.

    pytest test_app.py

Uses Flask's own test_client(), no running server needed, same client
test.py::check_service already uses. Each test starts from a clean audit
log (audit.clear()) so results from one test can't leak into another.

Submissions use a unique creator_id per test. Rate limiting (unit 8) keys
on creator_id when one is present, so this keeps every test's requests in
their own bucket instead of sharing one counter and tripping a 429 that
has nothing to do with what the test is checking.
"""

import itertools

import pytest

import app as appmod
import config

TEXT = "This is a plain test submission with enough words in it."

_creator_ids = (f"test-creator-{i}" for i in itertools.count())


@pytest.fixture(autouse=True)
def isolated_log(tmp_path, monkeypatch):
    """Point the audit log at a throwaway file so tests never touch the
    real logs/audit.jsonl — audit.clear() would otherwise wipe it."""
    monkeypatch.setattr(config, "LOG_DIR", tmp_path)
    monkeypatch.setattr(config, "AUDIT_LOG", tmp_path / "audit.jsonl")
    yield


@pytest.fixture
def client():
    return appmod.app.test_client()


def submit(client, creator_id=None):
    creator_id = creator_id or next(_creator_ids)
    response = client.post("/submit", json={"text": TEXT, "creator_id": creator_id})
    assert response.status_code == 200
    return response.get_json()["content_id"]


def appeal(client, content_id, reasoning="I wrote this myself."):
    response = client.post("/appeal", json={"content_id": content_id, "reasoning": reasoning})
    assert response.status_code == 200
    return response.get_json()


def test_queue_empty_on_clean_log(client):
    response = client.get("/queue")
    assert response.status_code == 200
    assert response.get_json() == {"count": 0, "queue": []}


def test_queue_has_appealed_item(client):
    content_id = submit(client)
    appeal(client, content_id, reasoning="This is my own writing.")

    response = client.get("/queue")
    assert response.status_code == 200
    body = response.get_json()
    assert body["count"] == 1
    assert body["queue"][0]["content_id"] == content_id
    assert body["queue"][0]["reasoning"] == "This is my own writing."
    assert body["queue"][0]["queued_since"]


def test_resolve_uphold_clears_queue_and_keeps_guess_label(client):
    content_id = submit(client)
    appeal(client, content_id)
    before = client.get(f"/content/{content_id}").get_json()

    response = client.post(f"/resolve/{content_id}", json={
        "decision": "uphold",
        "reviewer_id": "reviewer-1",
    })
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == "resolved"
    assert body["guess"] == before["guess"]
    assert body["label"] == before["label"]

    assert client.get("/queue").get_json()["count"] == 0

    after = client.get(f"/content/{content_id}").get_json()
    assert after["status"] == "resolved"
    assert after["guess"] == before["guess"]
    assert after["label"] == before["label"]


def test_resolve_overturn_sets_corrected_guess_label(client):
    content_id = submit(client)
    appeal(client, content_id)

    response = client.post(f"/resolve/{content_id}", json={
        "decision": "overturn",
        "reviewer_id": "reviewer-1",
        "corrected_guess": "human",
    })
    assert response.status_code == 200
    body = response.get_json()
    assert body["guess"] == "human"

    after = client.get(f"/content/{content_id}").get_json()
    assert after["guess"] == "human"
    assert after["label"] == body["label"]


def test_resolve_never_appealed_is_conflict(client):
    content_id = submit(client)

    response = client.post(f"/resolve/{content_id}", json={
        "decision": "uphold",
        "reviewer_id": "reviewer-1",
    })
    assert response.status_code == 409


def test_resolve_twice_is_conflict(client):
    content_id = submit(client)
    appeal(client, content_id)

    first = client.post(f"/resolve/{content_id}", json={
        "decision": "uphold",
        "reviewer_id": "reviewer-1",
    })
    assert first.status_code == 200

    second = client.post(f"/resolve/{content_id}", json={
        "decision": "uphold",
        "reviewer_id": "reviewer-1",
    })
    assert second.status_code == 409


def test_resolve_bad_decision_value_is_bad_request(client):
    content_id = submit(client)
    appeal(client, content_id)

    response = client.post(f"/resolve/{content_id}", json={
        "decision": "maybe",
        "reviewer_id": "reviewer-1",
    })
    assert response.status_code == 400


def test_resolve_unknown_content_id_is_not_found(client):
    response = client.post("/resolve/c_does_not_exist", json={
        "decision": "uphold",
        "reviewer_id": "reviewer-1",
    })
    assert response.status_code == 404
