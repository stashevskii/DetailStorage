from pydantic import Field
from pydantic_settings import BaseSettings

from .base.config import ConfigBase


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


class DetailRouterConfig:
    prefix: str = "/api/details"
    tags: list[str] = ["Details"]
    docs: dict[int: dict[str: str]] = {
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


class UserRouterConfig:
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
            "description": "Full update user endpoint"
        },
        5: {
            "summary": "Part update user",
            "description": "Part update user endpoint"
        }
    }


class SearchRouterConfig:
    prefix: str = "/api/details"
    tags: list[str] = ["Search details"]
    docs: dict[int: dict[str: str]] = {
        1: {
            "summary": "Get detail by lego id (parsing lego.com)",
            "description": "Get detail by lego id (parsing lego.com) endpoint"
        },
        2: {
            "summary": "Get detail by name (parsing lego.com)",
            "description": "Get detail by name (parsing lego.com) endpoint"
        },
    }


class CountryConfig:
    required_countries: set[str] = {'China', 'Denmark'}


class Config(BaseSettings):
    db_config: DbConfig = DbConfig()
    app_config: AppConfig = AppConfig()
    detail_router_config: DetailRouterConfig = DetailRouterConfig()
    user_router_config: UserRouterConfig = UserRouterConfig()
    search_router_config: SearchRouterConfig = SearchRouterConfig()
    country_config: CountryConfig = CountryConfig()


config = Config()
