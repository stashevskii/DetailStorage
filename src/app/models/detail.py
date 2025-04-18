from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from src.app.db.db import Base


class Detail(Base):
    __tablename__ = "details"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lego_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(30), nullable=True)

    def __init__(self, lego_id, name, quantity, id=None, description=None):
        self.id = id
        self.lego_id = lego_id
        self.name = name
        self.quantity = quantity
        self.description = description

    def __repr__(self):
        return f"Detail(id={self.id}, lego_id={self.lego_id}, name={self.name}, quantity={self.quantity}, description={self.description})"
