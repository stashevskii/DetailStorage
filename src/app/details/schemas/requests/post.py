from pydantic import Field
from typing import Optional
from src.app.bases.base_schema import BaseSchema


class AddDetailSchemaRequest(BaseSchema):
    id: Optional[int] = Field(ge=0, default=None)
    country_id: int = Field(ge=1, default=None)
    lego_id: int = Field(ge=0, default=None)
    name: str = Field(max_length=30, default=None)
    quantity: int = Field(ge=0, default=None)
    description: Optional[str] = Field(max_length=30, default=None)
