from pydantic import Field
from src.app.core.base import ConfigBase


class AppConfig(ConfigBase):
    app_debug: bool = Field()
    app_title: str = Field()
    app_description: str = Field()
    app_version: str = Field()
    app_host: str = Field()
    app_port: int = Field()
