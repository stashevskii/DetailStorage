from pydantic import Field
from typing import Optional
from src.app.entities.base import DetailStorageBase


class AddDetailSchemaRequest(DetailStorageBase):
    id: Optional[int] = Field(ge=0, default=None)
    lego_id: int = Field(ge=0, default=None)
    name: str = Field(max_length=30, default=None)
    quantity: int = Field(ge=0, default=None)
    description: Optional[str] = Field(max_length=30, default=None)
