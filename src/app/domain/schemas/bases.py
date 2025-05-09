from typing import Optional

from pydantic import Field, EmailStr

from src.app.core.base import BaseSchema
from src.app.infrastructure.config import config


class DetailBase(BaseSchema):
    country_id: int = Field(ge=1, le=len(config.country_config.required_countries))
    lego_id: int = Field(ge=0)
    name: str = Field(max_length=30)
    quantity: int = Field(ge=0)
    description: Optional[str] = Field(max_length=30, default=None)


class DetailBaseOptional(BaseSchema):
    country_id: Optional[int] = Field(ge=1, le=len(config.country_config.required_countries), default=None)
    lego_id: Optional[int] = Field(ge=1, default=None)
    name: Optional[str] = Field(max_length=30, default=None)
    quantity: Optional[int] = Field(ge=0, default=None)
    description: Optional[str] = Field(max_length=30, default=None)


class UserBase(BaseSchema):
    username: str = Field(min_length=4, max_length=30)
    email: EmailStr = Field()


class UserBaseOptional(BaseSchema):
    username: Optional[str] = Field(min_length=4, max_length=30, default=None)
    email: Optional[EmailStr] = Field(default=None)


class UserBasePassword(UserBase):
    password: str = Field(min_length=4, max_length=20)


class PageLimitSchema(BaseSchema):
    page_limit: int = Field(ge=1, le=15)
