def test_remove_participant_removes_existing(client):
    # Arrange
    activity = "Programming Class"
    email = "temp_remove@example.com"
    participants = client.get("/activities").json()[activity]["participants"]
    if email not in participants:
        client.post(f"/activities/{activity}/signup", params={"email": email})

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert "Removed" in resp.json().get("message", "")
    participants_after = client.get("/activities").json()[activity]["participants"]
    assert email not in participants_after
