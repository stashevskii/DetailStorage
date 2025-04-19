from pydantic import Field
from typing import Optional
from src.app.dtos.base import DetailStorageBase


class FullUpdateDetailDtoRequest(DetailStorageBase):
    new_lego_id: int = Field(ge=0, default=None)
    country_id: Optional[int] = Field(ge=1, default=None)
    new_name: str = Field(max_length=30, default=None)
    new_quantity: int = Field(ge=0, default=None)
    new_description: Optional[str] = Field(max_length=30, default=None)
