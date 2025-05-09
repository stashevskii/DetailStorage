from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.app.infrastructure.persistence.db import Base


class Detail(Base):
    __tablename__ = "details"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country_id: Mapped[int] = mapped_column(Integer, ForeignKey("countries.id"), nullable=False)
    country: Mapped["Country"] = relationship("Country", back_populates="details")
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="details")
    lego_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(30), nullable=True)

    def __repr__(self):
        return f"Detail(id={self.id}, country_id={self.country_id}, user_id={self.user_id}, lego_id={self.lego_id}, name={self.name}, quantity={self.quantity}, description={self.description})"
