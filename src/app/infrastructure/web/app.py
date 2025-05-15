import logging
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from src.app.infrastructure.config import config
from src.app.api.errors import register_exceptions_handler
from src.app.api.routes import register_main_router
from src.app.infrastructure.persistence.db import engine
from src.app.core.base import Base
from src.app.core.utils import create_required_countries
from src.app.core.utils import configure_logging, get_logger
from .middlewares import register_middlewares

log = get_logger(__name__)


@asynccontextmanager
async def lifespan(application: FastAPI):
    configure_logging(logging.INFO)
    Base.metadata.create_all(bind=engine)
    log.info("Created all tables in db")
    create_required_countries()

    yield


def create_app() -> FastAPI:
    application = FastAPI(
        debug=config.app_config.app_debug,
        title=config.app_config.app_title,
        version=config.app_config.app_version,
        description=config.app_config.app_description,
        lifespan=lifespan
    )
    register_main_router(application)
    register_middlewares(application)
    register_exceptions_handler(application)
    return application


def run():
    uvicorn.run(
        app="src.app.main:app",
        host=config.app_config.app_host,
        port=config.app_config.app_port,
        log_config=None,
        access_log=False,
        reload=True
    )


app = create_app()
