from src.app.core.base import ConfigBase


class AppConfig(ConfigBase):
    app_debug: bool
    app_title: str
    app_description: str
    app_version: str
    app_host: str
    app_port: int
