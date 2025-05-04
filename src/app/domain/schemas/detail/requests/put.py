from pydantic import Field
from typing import Optional
from src.app.core.common.schema import BaseSchema
from src.app.core.config import config


class FullUpdateDetailSchemaRequest(BaseSchema):
    new_lego_id: int = Field(ge=0)
    new_country_id: int = Field(ge=1, le=len(config.country_config.required_countries))
    new_name: str = Field(max_length=30)
    new_quantity: int = Field(ge=0)
    new_description: Optional[str] = Field(max_length=30, default=None)
