from pydantic import Field, EmailStr
from src.app.core.common.schema import BaseSchema


class FullUpdateUserSchemaRequest(BaseSchema):
    username: str = Field(min_length=4, max_length=30)
    password: str = Field(min_length=4, max_length=20)
    email: EmailStr = Field()
