from typing import Optional

from fastapi import APIRouter, FastAPI
from pydantic import Field
from ..config import *
from .funcs import *
from src.app.core.common.schema import BaseSchema


class TestSchema(BaseSchema):
    id: Optional[int] = Field(ge=0, default=None)
    country_id: int = Field(ge=1, default=None)
    lego_id: int = Field(ge=0, default=None)
    name: str = Field(max_length=30, default=None)
    quantity: int = Field(ge=0, default=None)
    description: Optional[str] = Field(max_length=30, default=None)

router = APIRouter(prefix=prefix, tags=tags)

router.get("/", summary=docs[1]["summary"], description=docs[1]["description"])(get_detail)
router.post("/", summary=docs[2]["summary"], description=docs[2]["description"])(add_detail)
router.delete("/{id}", summary=docs[3]["summary"], description=docs[3]["description"])(delete_detail)
router.put("/{id}", summary=docs[4]["summary"], description=docs[4]["description"])(full_update_detail)
router.patch("/{id}", summary=docs[5]["summary"], description=docs[5]["description"])(part_update_detail)


def add_detail_router(app: FastAPI):
    app.include_router(router)
