from .logger import get_logger
from src.app.infrastructure.config import config
from src.app.infrastructure.persistence.db import get_db
from src.app.infrastructure.persistence.models import Country

log = get_logger(__name__)


def create_required_countries() -> None:
    session = get_db()

    existing = {c.name for c in session.query(Country.name).all()}
    missing = config.country_config.required_countries - existing

    for country in missing:
        session.add(Country(name=country))

    session.query(Country).filter(Country.name.notin_(config.country_config.required_countries)).delete()
    session.commit()
    log.info("Created required countries in db")
