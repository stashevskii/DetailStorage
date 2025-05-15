from src.app.core.base import ConfigBase


class DbConfig(ConfigBase):
    db_username: str
    db_password: str
    db_host: str
    db_name: str
