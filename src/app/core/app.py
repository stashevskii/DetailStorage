from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from src.app.core.config import config
from src.app.api.errors.register import register_exceptions_handler
from src.app.api.endpoints import router
from src.app.db.db import engine, Base
from src.app.utils.required_countries import create_required_countries


@asynccontextmanager
async def lifespan(application: FastAPI):
    Base.metadata.create_all(bind=engine)
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
    application.include_router(router)
    register_exceptions_handler(application)
    return application


def run():
    uvicorn.run("src.app.main:app", host=config.app_config.app_host, port=config.app_config.app_port, reload=True)


app = create_app()
