from app.config import get_config
from pydantic_settings import BaseSettings


def test_config_returns_model() -> None:
    config = get_config()
    assert isinstance(config, BaseSettings)
