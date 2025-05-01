from pydantic import Field, EmailStr
from typing import Optional
from src.app.users.core.common.schema import BaseSchema


class GetUserSchemaRequest(BaseSchema):
    id: Optional[int] = Field(ge=0, default=None)
    username: Optional[str] = Field(min_length=4, max_length=30, default=None)
    email: Optional[EmailStr] = Field(default=None)
    all_obj: Optional[bool] = Field(default=False)
