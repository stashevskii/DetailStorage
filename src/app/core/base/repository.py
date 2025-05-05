from typing import Type
from sqlalchemy.orm import Session
from src.app.infrastructure.persistence.db import Base


class Repository:
    def __init__(self, session: Session):
        self.session = session
        self.table: Type[Base]
