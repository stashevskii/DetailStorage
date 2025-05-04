from typing import Optional
from pydantic import Field
from src.app.core.common.schema import BaseSchema
from src.app.core.config import config


class DetailBase(BaseSchema):
    country_id: int = Field(ge=1, le=len(config.country_config.required_countries))
    lego_id: int = Field(ge=0)
    name: str = Field(max_length=30)
    quantity: int = Field(ge=0)
    description: Optional[str] = Field(max_length=30)


class DetailBaseOptional(BaseSchema):
    country_id: Optional[int] = Field(ge=1, default=None)
    lego_id: Optional[int] = Field(ge=0, le=len(config.country_config.required_countries), default=None)
    name: Optional[str] = Field(max_length=30, default=None)
    quantity: Optional[int] = Field(ge=0, default=None)
    description: Optional[str] = Field(max_length=30, default=None)
