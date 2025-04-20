from .success import SuccessResponseSchema
from typing import Optional
from pydantic import Field


class BaseResponseSchema(SuccessResponseSchema):
    id: Optional[int] = Field(ge=0, default=None)
