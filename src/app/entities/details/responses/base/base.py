from .success import SuccessResponseModel
from typing import Optional
from pydantic import Field


class BaseResponseModel(SuccessResponseModel):
    id: Optional[int] = Field(ge=0, default=None)
