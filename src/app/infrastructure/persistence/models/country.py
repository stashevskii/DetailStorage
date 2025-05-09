from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.app.core.base import Base


class Country(Base):
    __tablename__ = "countries"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    details: Mapped[list["Detail"]] = relationship("Detail", back_populates="country")
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f"Country(id={self.id}, name={self.name})"
