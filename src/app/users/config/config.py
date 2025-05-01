from pydantic import Field

from src.app.users.core.common.config import ConfigBase


class DbConfig(ConfigBase):
    db_Username: str = Field()
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


class RouterConfig:
    prefix: str = "/api/users"
    tags: list[str] = ["Users"]
    docs: dict[int: dict[str: str]] = {
        1: {
            "summary": "Get users by parameters",
            "description": "Get users by parameters endpoint"
        },
        2: {
            "summary": "Add new user",
            "description": "Add new user endpoint"
        },
        3: {
            "summary": "Delete user",
            "description": "Delete user endpoint"
        },
        4: {
            "summary": "Full update user",
            "description": "Full update Users endpoint"
        },
        5: {
            "summary": "Part update user",
            "description": "Part update User endpoint"
        }
    }


db_config = DbConfig()
app_config = AppConfig()
router_config = RouterConfig()
