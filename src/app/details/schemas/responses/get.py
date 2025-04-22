from pydantic import Field
from typing import Optional
from src.app.core.common.schema import BaseSchema


class GetDetailSchemaResponse(BaseSchema):
    id: Optional[int] = Field(ge=0)
    country_id: Optional[int] = Field(ge=1)
    lego_id: Optional[int] = Field(ge=0)
    name: Optional[str] = Field(max_length=30)
    quantity: Optional[int] = Field(ge=0)
    description: Optional[str] = Field(max_length=30)
