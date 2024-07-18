from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from functools import cache


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=f".{os.environ.get("FAST_API_ENV")}.env")


@cache
def get_config() -> Config:
    return Config()
