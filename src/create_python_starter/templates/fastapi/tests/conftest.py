import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture()
def client() -> TestClient:
    """`FastAPI` testing client.

    This object can be used to interact with the server
    within tests.

    ```python
        from fastapi import FastAPI
        from fastapi.testclient import TestClient

        app = FastAPI()


        @app.get("/")
        async def read_main():
            return {"msg": "Hello World"}


        client = TestClient(app)


        def test_read_main():
            response = client.get("/")
            assert response.status_code == 200
            assert response.json() == {"msg": "Hello World"}
    ```
    Returns:
        `TestClient`
    """
    return TestClient(app)
