from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app.infrastructure.config import config

engine = create_engine(
    f"postgresql://{config.db_config.db_username}:{config.db_config.db_password}@{config.db_config.db_host}/{config.db_config.db_name}"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
