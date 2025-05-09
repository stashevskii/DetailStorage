import logging
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from src.app.infrastructure.config import config
from src.app.api.errors import register_exceptions_handler
from src.app.api.endpoints import include_main_router
from src.app.infrastructure.persistence.db import engine
from src.app.core.base import Base
from src.app.core.utils import create_required_countries
from src.app.core.utils import configure_logging, get_logger

log = get_logger(__name__)


@asynccontextmanager
async def lifespan(application: FastAPI):
    configure_logging(logging.INFO)
    Base.metadata.create_all(bind=engine)
    log.info("Created tables in db")
    create_required_countries()
    log.info("Created required countries in db table countries")

    yield


def create_app() -> FastAPI:
    application = FastAPI(
        debug=config.app_config.app_debug,
        title=config.app_config.app_title,
        version=config.app_config.app_version,
        description=config.app_config.app_description,
        lifespan=lifespan
    )
    include_main_router(application)
    register_exceptions_handler(application)
    return application


def run():
    uvicorn.run("src.app.main:app", host=config.app_config.app_host, port=config.app_config.app_port, reload=True)


app = create_app()
