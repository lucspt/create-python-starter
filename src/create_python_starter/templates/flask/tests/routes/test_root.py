from flask.testing import FlaskClient


def test_root_get(client: FlaskClient) -> None:
    res = client.get("/")
    assert res.status_code == 200
