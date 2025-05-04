from src.app.core.config import config
from src.app.db.db import Base, engine, get_db
from src.app.domain.models.country import Country


def create_required_countries():
    session = get_db()

    existing = {c.name for c in session.query(Country.name).all()}
    missing = config.country_config.required_countries - existing

    for country in missing:
        session.add(Country(name=country))

    session.query(Country).filter(Country.name.notin_(config.country_config.required_countries)).delete()
    session.commit()
