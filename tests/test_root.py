def test_root_redirect(client):
    # Arrange: none (app mounts static files)

    # Act: don't follow redirects to verify redirect response
    resp = client.get("/", follow_redirects=False)

    # Assert
    assert resp.status_code in (301, 302, 307, 308)
    assert resp.headers.get("location", "").endswith("/static/index.html")
