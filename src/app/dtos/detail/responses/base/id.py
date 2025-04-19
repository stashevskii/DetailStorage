from .success import SuccessResponseDto
from typing import Optional
from pydantic import Field


class BaseResponseDto(SuccessResponseDto):
    id: Optional[int] = Field(ge=0, default=None)
