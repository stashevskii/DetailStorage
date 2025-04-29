from pydantic import Field
from src.app.search.core.common.config import ConfigBase


class AppConfig(ConfigBase):
    app_debug: bool = Field()
    app_title: str = Field()
    app_description: str = Field()
    app_version: str = Field()
    app_host: str = Field()
    app_port: int = Field()


class RouterConfig:
    prefix: str = "/api/details"
    tags = ["Detail search"]
    docs: dict[int: dict[str, str]] = {
        1: {
            "summary": "Search detail (parsing lego.com) by name",
            "description": "Search detail by name endpoint"
        },
        2: {
            "summary": "Search detail (parsing lego.com) by lego id",
            "description": "Search detail by lego id endpoint"
        },
    }


app_config = AppConfig()
router_config = RouterConfig()
