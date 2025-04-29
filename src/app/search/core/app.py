import uvicorn
from fastapi import FastAPI
from src.app.search.routes.router import router
from src.app.search.config.config import app_config
from src.app.search.exceptions.register import register_exceptions_handler


def create_app() -> FastAPI:
    app_ = FastAPI(
        debug=app_config.app_debug,
        title=app_config.app_title,
        version=app_config.app_version,
        description=app_config.app_description,
    )
    app_.include_router(router)
    register_exceptions_handler(app_)
    return app_



def run():
    uvicorn.run("src.app.search.bin.main:app", host=app_config.app_host, port=app_config.app_port, reload=True)


app = create_app()
