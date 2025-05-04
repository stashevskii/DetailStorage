from pydantic import Field, EmailStr
from typing import Optional
from src.app.core.common.schema import BaseSchema


class PartUpdateUserSchemaRequest(BaseSchema):
    username: Optional[str] = Field(min_length=4, max_length=30)
    password: Optional[str] = Field(min_length=4, max_length=20)
    email: Optional[EmailStr] = Field()
