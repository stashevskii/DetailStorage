from pydantic import Field
from typing import Optional
from src.app.bases.base_schema import BaseSchema


class GetDetailSchemaResponse(BaseSchema):
    id: Optional[int] = Field(ge=0)
    country_id: Optional[int] = Field(ge=1, default=None)
    lego_id: Optional[int] = Field(ge=0)
    name: Optional[str] = Field(max_length=30)
    quantity: Optional[int] = Field(ge=0)
    description: Optional[str] = Field(max_length=30)
