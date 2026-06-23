def test_signup_adds_participant_and_is_idempotent(client):
    # Arrange
    activity = "Chess Club"
    email = "test_user@example.com"
    # Ensure email not present
    participants = client.get("/activities").json()[activity]["participants"]
    if email in participants:
        client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert "Signed up" in resp.json().get("message", "")
    participants_after = client.get("/activities").json()[activity]["participants"]
    assert email in participants_after

    # Cleanup
    client.delete(f"/activities/{activity}/participants", params={"email": email})
