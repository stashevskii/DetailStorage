from typing import Optional
from pydantic import Field
from .bases import (
    DetailBase, UserBasePassword, UserBase,
    UserBaseOptional, DetailBaseOptional, PageLimitSchema
)
from src.app.core.base.schema import BaseSchema


# Country schema
class CountrySchema(BaseSchema):
    id: int = Field(ge=1)
    name: str = Field(min_length=1)


# User lite schema (fixes linked imports bug)
class UserLiteSchema(UserBase):
    id: int = Field(ge=0)


# Detail schemas
class DetailSchema(DetailBase):
    id: int = Field(ge=0)
    user: UserLiteSchema
    country: CountrySchema


class DetailFilter(DetailBaseOptional):
    user_id: Optional[int] = Field(ge=1, default=None)
    id: Optional[int] = Field(ge=0, default=None)
    all_obj: bool = Field(default=False)


class DetailCreate(DetailBase):
    user_id: int = Field(ge=1)
    id: Optional[int] = Field(ge=0, default=None)


class DetailFullUpdate(DetailBase): ...


class DetailPartUpdate(DetailBaseOptional): ...


class UserSchema(UserBase):
    id: int = Field(ge=0)
    details: list[DetailSchema]


class UserCreate(UserBasePassword):
    id: Optional[int] = Field(ge=0, default=None)


class UserFilter(UserBaseOptional):
    id: Optional[int] = Field(ge=0, default=None)


class UserPartUpdate(UserBaseOptional):
    password: Optional[str] = Field(min_length=4, max_length=20, default=None)


class UserFullUpdate(UserBasePassword): ...


# Search schemas
class DetailName(PageLimitSchema):
    name: str = Field(min_length=1)


class DetailLegoId(PageLimitSchema):
    lego_id: int = Field(ge=0)
