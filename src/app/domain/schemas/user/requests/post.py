from pydantic import Field, EmailStr
from typing import Optional
from src.app.core.common.schema import BaseSchema


class AddUserSchemaRequest(BaseSchema):
    id: Optional[int] = Field(ge=0, default=None)
    username: str = Field(min_length=4, max_length=30)
    password: str = Field(min_length=4, max_length=20)
    email: EmailStr = Field()


class AddUserSchemaRequestWithHashedPassword(BaseSchema):
    id: Optional[int] = Field(ge=0, default=None)
    username: str = Field(min_length=4, max_length=30)
    hashed_password: bytes = Field()
    email: EmailStr = Field()
