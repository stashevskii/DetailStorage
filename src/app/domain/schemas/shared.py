from typing import Optional
from pydantic import Field
from src.app.core.base.schema import BaseSchema


class SuccessSchema(BaseSchema):
    success: bool = None


class BaseResponseSchema(SuccessSchema):
    id: Optional[int] = Field(ge=0, default=None)
