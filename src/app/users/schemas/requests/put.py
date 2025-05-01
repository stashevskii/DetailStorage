from pydantic import Field
from typing import Optional
from src.app.users.core.common.schema import BaseSchema


class FullUpdateUserSchemaRequest(BaseSchema):
    new_lego_id: int = Field(ge=0)
    new_country_id: int = Field(ge=1)
    new_name: str = Field(max_length=30)
    new_quantity: int = Field(ge=0)
    new_description: Optional[str] = Field(max_length=30, default=None)
