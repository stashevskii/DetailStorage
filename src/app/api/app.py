from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from sqlalchemy import delete
from src.app.core.exceptions import exception_handlers
from src.app.api.routes.detail.router import add_detail_router
from src.app.core.config import app_config
from src.app.db.db import engine, Base, get_db
from src.app.models.detail import Detail
from src.app.models.country import Country


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
    return FastAPI(
        debug=app_config.app_debug,
        title=app_config.app_title,
        version=app_config.app_version,
        description=app_config.app_description,
        exception_handlers=exception_handlers,
        lifespan=lifespan
    )


def run():
    uvicorn.run("src.app.main:app", host=app_config.app_host, port=app_config.app_port, reload=True)


app = create_app()
add_detail_router(app)
