from pytest import fixture
from app import create_app
from flask import Flask
from flask.testing import FlaskClient
from typing import Generator


@fixture()
def app() -> Generator[Flask, None, None]:
    """Access the Flask server instance"""
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@fixture()
def client(app: Flask) -> FlaskClient:
    """Get the Flask test client.

    This object can be used to make mock requests to the application.

    Usage:
    ```
        res = client.get("/")
        assert isinstance(res, Response)
        assert res.status_code == 200
        # more tests here...
    ```

    See more here: https://flask.palletsprojects.com/en/2.3.x/testing/
    """
    return app.test_client()
