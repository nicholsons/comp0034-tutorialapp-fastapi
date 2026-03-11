from __future__ import annotations

import os
import secrets
from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[3]


class SettingsBase(BaseSettings):
    """ Settings class with values for all environments"""
    db_name: str
    db_driver: str
    algorithm: str
    access_token_expires: int

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=False,
        extra="ignore"
    )

    @property
    def database_url(self) -> str:
        db_path = BASE_DIR / "src" / "data" / self.db_name
        return f"{self.db_driver}{db_path}"


class SettingsDevelopment(SettingsBase):
    """ Settings class with values for development environment"""
    db_name: str
    secret_key: str = secrets.token_urlsafe(32)


class SettingsTest(SettingsBase):
    """ Settings class with values for the testing environment"""
    db_name: str = Field(validation_alias="test_db")
    secret_key: str = "some-other-super-secret-key-for-testing"


@lru_cache()
def get_settings():
    env = os.getenv("ENV", "development")
    config_cls_dict = {"development": SettingsDevelopment,
                       "testing": SettingsTest}
    config_cls = config_cls_dict[env]
    return config_cls()


settings = get_settings()
