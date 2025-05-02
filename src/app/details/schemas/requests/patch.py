from pydantic import Field
from typing import Optional

from src.app.details.config.config import CountryConfig
from src.app.details.core.common.schema import BaseSchema


class PartUpdateDetailSchemaRequest(BaseSchema):
    lego_id: Optional[int] = Field(ge=0, default=None)
    country_id: Optional[int] = Field(ge=1, le=len(CountryConfig.required_countries), default=None)
    name: Optional[str] = Field(max_length=30, default=None)
    quantity: Optional[int] = Field(ge=0, default=None)
    description: Optional[str] = Field(max_length=30, default=None)
