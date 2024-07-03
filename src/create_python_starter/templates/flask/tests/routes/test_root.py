from flask.testing import FlaskClient


def test_root_get(api: FlaskClient) -> None:
    res = api.get("/")
    assert res.status_code == 200
