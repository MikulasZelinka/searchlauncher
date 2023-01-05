from functools import lru_cache
from pathlib import Path
from typing import Any

from loguru import logger
from pydantic import BaseModel, BaseSettings, HttpUrl
from pydantic.env_settings import SettingsSourceCallable
from tomlkit import load

# this file → this folder → settings folder → default.toml
DEFAULT_SETTINGS_PATH = Path(__file__).parent / "settings" / "default.toml"


class SearchGroup(BaseModel):
    shortcut: str = ""
    sites: list[str] = []
    groups: list[str] = []


def toml_settings(settings: BaseSettings) -> dict[str, Any]:
    """
    A simple settings source that loads variables from a JSON file
    at the project's root.

    Here we happen to choose to use the `env_file_encoding` from Config
    when reading `config.json`
    """
    logger.debug(f"Loading settings from {DEFAULT_SETTINGS_PATH}")

    with open(DEFAULT_SETTINGS_PATH) as f:
        settings = load(f)
    return settings


class Settings(BaseSettings):
    shortcut: str
    sites: dict[str, HttpUrl]
    groups: dict[str, SearchGroup]

    class Config:
        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> tuple[SettingsSourceCallable, ...]:
            return init_settings, toml_settings


@lru_cache()
def load_settings(**kwargs) -> Settings:  # type: ignore
    return Settings(**kwargs)


if __name__ == "__main__":
    settings = load_settings()
    print(settings)
