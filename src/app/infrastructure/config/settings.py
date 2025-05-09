from pydantic_settings import BaseSettings
from .app import AppConfig
from .countries import CountryConfig
from .db import DbConfig
from .routers import DetailRouterConfig, SearchRouterConfig, UserRouterConfig


class Config(BaseSettings):
    db_config: DbConfig = DbConfig()
    app_config: AppConfig = AppConfig()
    detail_router_config: DetailRouterConfig = DetailRouterConfig()
    user_router_config: UserRouterConfig = UserRouterConfig()
    search_router_config: SearchRouterConfig = SearchRouterConfig()
    country_config: CountryConfig = CountryConfig()


config = Config()
