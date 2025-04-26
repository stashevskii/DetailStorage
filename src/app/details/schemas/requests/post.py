from pydantic import Field
from typing import Optional
from src.app.details.core.common.schema import BaseSchema


class AddDetailSchemaRequest(BaseSchema):
    id: Optional[int] = Field(ge=0, default=None)
    country_id: int = Field(ge=1)
    lego_id: int = Field(ge=0)
    name: str = Field(max_length=30)
    quantity: int = Field(ge=0)
    description: Optional[str] = Field(max_length=30, default=None)
