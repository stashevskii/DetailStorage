from pydantic import Field, EmailStr
from src.app.core.common.schema import BaseSchema


class GetUserSchemaResponse(BaseSchema):
    id: int = Field(ge=0, default=None)
    username: str = Field(min_length=4, max_length=30, default=None)
    email: EmailStr = Field(default=None)
