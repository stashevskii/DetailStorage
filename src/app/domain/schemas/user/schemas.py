from pydantic import Field
from typing import Optional

from ..detail import DetailSchema
from .bases import UserBase, UserBaseOptional, UserBasePassword


class UserSchema(UserBase):
    id: int = Field(ge=0)
    details: list[DetailSchema] = []


class UserCreate(UserBasePassword): id: Optional[int] = Field(ge=0, default=None)


class UserFilter(UserBaseOptional): id: Optional[int] = Field(ge=0, default=None)


class UserPartUpdate(UserBaseOptional): password: Optional[str] = Field(min_length=4, max_length=20, default=None)


class UserFullUpdate(UserBasePassword): ...
