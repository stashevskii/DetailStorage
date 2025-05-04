from pydantic import Field
from typing import Optional
from src.app.core.common.schema import BaseSchema
from src.app.core.config import config


class GetDetailSchemaRequest(BaseSchema):
    id: Optional[int] = Field(ge=0, default=None)
    country_id: Optional[int] = Field(ge=1, default=None)
    user_id: Optional[int] = Field(ge=1, default=None)
    lego_id: Optional[int] = Field(ge=0, le=len(config.country_config.required_countries), default=None)
    name: Optional[str] = Field(max_length=30, default=None)
    quantity: Optional[int] = Field(ge=0, default=None)
    description: Optional[str] = Field(max_length=30, default=None)
    all_obj: bool = Field(default=False)
