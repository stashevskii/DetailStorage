from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from .exceptions import global_exception_handlers
from src.app.details.routes.router import add_detail_router
from src.app.config import app_config
from src.app.db import engine, get_db
from src.app.details.models.country import Country
from bases.base_model import Base


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
        exception_handlers=global_exception_handlers,
        lifespan=lifespan
    )
    add_detail_router(app_)
    return app_


def run():
    uvicorn.run("src.app.main:app", host=app_config.app_host, port=app_config.app_port, reload=True)


app = create_app()
