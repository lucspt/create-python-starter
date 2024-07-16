from fastapi.testclient import TestClient

def test_get_root(client: TestClient) -> None:
    res = client.get("/")
    assert res.status_code == 200
    