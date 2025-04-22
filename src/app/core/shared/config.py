from pydantic import Field
from src.app.core.common.config import ConfigBase


class DbConfig(ConfigBase):
    db_username: str = Field()
    db_password: str = Field()
    db_host: str = Field()
    db_name: str = Field()


class AppConfig(ConfigBase):
    app_debug: bool = Field()
    app_title: str = Field()
    app_description: str = Field()
    app_version: str = Field()
    app_host: str = Field()
    app_port: int = Field()


db_config = DbConfig()
app_config = AppConfig()
