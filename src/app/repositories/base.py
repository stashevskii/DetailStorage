from sqlalchemy.orm import Session

from src.app.models.detail import Detail


class Repository:
    def __init__(self, session: Session, table):
        self.session = session
        self.table = table
