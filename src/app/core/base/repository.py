from sqlalchemy.orm import Session


class Repository[T]:
    def __init__(self, session: Session):
        self.session = session
        self.table: T
