from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent.parent.parent.parent / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
