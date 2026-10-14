from app import validate_ticket

def test_title_too_long():
    error = validate_ticket("A" * 21, "A101")
    assert error == "标题不能超过20个字符"

def test_post_title_too_long(client):
    resp = client.post("/tickets/new", data={"title": "A" * 21, "room": "A区101", "description": "测试"})
    assert resp.status_code == 400
    assert "标题不能超过20个字符" in resp.data.decode()
