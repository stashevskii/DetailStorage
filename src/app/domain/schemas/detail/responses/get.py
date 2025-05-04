from pydantic import Field
from typing_extensions import Optional
from src.app.core.common.schema import BaseSchema


class GetDetailSchemaResponse(BaseSchema):
    id: int = Field(ge=0)
    country_id: int = Field(ge=1)
    user_id: int = Field(ge=1)
    lego_id: int = Field(ge=0)
    name: str = Field(max_length=30)
    quantity: int = Field(ge=0)
    description: Optional[str] = Field(max_length=30)
