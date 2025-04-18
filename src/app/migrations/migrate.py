from src.app.db.db import Base, engine, get_db
from src.app.models.detail import Detail

Base.metadata.create_all(bind=engine)
