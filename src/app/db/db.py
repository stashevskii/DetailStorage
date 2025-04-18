from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.app.core.config import db_config

engine = create_engine(
    f"postgresql://{db_config.db_username}:{db_config.db_password}@{db_config.db_host}/{db_config.db_name}"
)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
