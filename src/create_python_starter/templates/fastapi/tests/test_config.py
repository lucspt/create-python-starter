from pydantic_settings import BaseSettings

from app.config import get_config


def test_config_returns_model() -> None:
    config = get_config()
    assert isinstance(config, BaseSettings)
