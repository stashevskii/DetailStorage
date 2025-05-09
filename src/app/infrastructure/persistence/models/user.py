from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.app.core.base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    hashed_password: Mapped[bytes] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    details: Mapped[list["Detail"]] = relationship("Detail", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"
