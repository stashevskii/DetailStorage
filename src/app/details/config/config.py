from pydantic import Field

from src.app.details.core.common.config import ConfigBase


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


class RouterConfig:
    prefix: str = "/api/details"
    tags: list[str] = ["Details"]
    docs: dict[int: dict[str: str, str: str]] = {
        1: {
            "summary": "Get details by parameters",
            "description": "Get details by parameters endpoint"
        },
        2: {
            "summary": "Add new details",
            "description": "Add new details endpoint"
        },
        3: {
            "summary": "Delete details",
            "description": "Delete details endpoint"
        },
        4: {
            "summary": "Full update details",
            "description": "Full update details endpoint"
        },
        5: {
            "summary": "Part update details",
            "description": "Part update details endpoint"
        }
    }


db_config = DbConfig()
app_config = AppConfig()
router_config = RouterConfig()
