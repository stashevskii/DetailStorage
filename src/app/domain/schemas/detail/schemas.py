from pydantic import Field
from typing import Optional
from src.app.domain.schemas.detail.bases import DetailBaseOptional, DetailBase


class DetailFilter(DetailBaseOptional):
    user_id: Optional[int] = Field(ge=1, default=None)
    id: Optional[int] = Field(ge=0, default=None)
    all_obj: bool = Field(default=False)


class DetailPartUpdate(DetailBaseOptional): ...


class DetailCreate(DetailBase):
    user_id: int = Field(ge=1)
    id: Optional[int] = Field(ge=0, default=None)


class DetailFullUpdate(DetailBase): ...


class DetailSchema(DetailBase):
    id: int = Field(ge=0)
