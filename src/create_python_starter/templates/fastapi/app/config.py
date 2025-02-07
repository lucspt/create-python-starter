import os
from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=f".{os.environ.get("FASTAPI_ENV")}.env")


@cache
def get_config() -> Config:
    return Config()
