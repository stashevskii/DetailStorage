from pydantic import Field
from src.app.core.base.config import ConfigBase


class DbConfig(ConfigBase):
    db_username: str = Field()
    db_password: str = Field()
    db_host: str = Field()
    db_name: str = Field()
