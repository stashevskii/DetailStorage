from sqlalchemy import Integer, String, inspect
from sqlalchemy.orm import mapped_column, Mapped
from src.app.users.core.db import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    hashed_password: Mapped[bytes] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    def __init__(self, username: str, hashed_password: bytes, email: str, id=None):
        self.id = id
        self.username = username
        self.hashed_password = hashed_password
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"

    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
