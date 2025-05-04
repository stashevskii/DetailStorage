from typing import Optional
from pydantic import EmailStr, Field
from src.app.core.base.schema import BaseSchema


class UserBase(BaseSchema):
    username: str = Field(min_length=4, max_length=30)
    email: EmailStr = Field()


class UserBasePassword(UserBase):
    password: str = Field(min_length=4, max_length=20)


class UserBaseOptional(BaseSchema):
    username: Optional[str] = Field(min_length=4, max_length=30, default=None)
    email: Optional[EmailStr] = Field(default=None)
