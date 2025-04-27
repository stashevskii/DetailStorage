from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from src.app.details.config.config import app_config
from src.app.details.exceptions.register import register_exceptions_handler
from src.app.details.routes.router import router
from src.app.details.core.db import engine, get_db, Base
from src.app.details.models.models import Country


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    session = get_db()
    required_countries = {'China', 'Denmark'}

    existing = {c.name for c in session.query(Country.name).all()}
    missing = required_countries - existing

    for country in missing:
        session.add(Country(name=country))

    session.query(Country).filter(Country.name.notin_(required_countries)).delete()
    session.commit()

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
    uvicorn.run("src.app.details.bin.main:app", host=app_config.app_host, port=app_config.app_port, reload=True)


app = create_app()
