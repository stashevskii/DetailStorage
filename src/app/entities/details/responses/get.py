from pydantic import Field
from typing import Optional
from src.app.entities.base import DetailStorageBase


class GetDetailSchemaResponse(DetailStorageBase):
    id: Optional[int] = Field(ge=0)
    lego_id: Optional[int] = Field(ge=0)
    name: Optional[str] = Field(max_length=30)
    quantity: Optional[int] = Field(ge=0)
    description: Optional[str] = Field(max_length=30)
