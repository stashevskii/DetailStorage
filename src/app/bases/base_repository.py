from sqlalchemy.orm import Session


class Repository:
    def __init__(self, session: Session, table):
        self.session = session
        self.table = table
