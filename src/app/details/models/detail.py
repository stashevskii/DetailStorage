from sqlalchemy import Integer, String, ForeignKey, inspect
from sqlalchemy.orm import mapped_column, Mapped
from src.app.bases.base_model import Base


class Detail(Base):
    __tablename__ = "details"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))
    lego_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(30), nullable=True)

    def __init__(self, lego_id, name, quantity, country_id, id=None, description=None):
        self.id = id
        self.country_id = country_id
        self.lego_id = lego_id
        self.name = name
        self.quantity = quantity
        self.description = description

    def __repr__(self):
        return f"Detail(id={self.id}, country_id={self.country_id}, lego_id={self.lego_id}, name={self.name}, quantity={self.quantity}, description={self.description})"

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
