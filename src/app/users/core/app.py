from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from src.app.users.config.config import app_config
from src.app.users.exceptions.register import register_exceptions_handler
from src.app.users.routes.router import router
from src.app.users.core.db import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


def create_app() -> FastAPI:
    app_ = FastAPI(
        debug=app_config.app_debug,
        title=app_config.app_title,
        version=app_config.app_version,
        description=app_config.app_description,
        lifespan=lifespan
    )
    app_.include_router(router)
    register_exceptions_handler(app_)
    return app_


def run():
    uvicorn.run("src.app.users.bin.main:app", host=app_config.app_host, port=app_config.app_port, reload=True)


app = create_app()
