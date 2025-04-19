from pydantic import Field
from typing import Optional
from src.app.dtos.base import DetailStorageBase


class GetDetailDtoRequest(DetailStorageBase):
    id: Optional[int] = Field(ge=0, default=None)
    lego_id: Optional[int] = Field(ge=0, default=None)
    name: Optional[str] = Field(max_length=30, default=None)
    quantity: Optional[int] = Field(ge=0, default=None)
    description: Optional[str] = Field(max_length=30, default=None)
    all_obj: bool = Field(default=False)
