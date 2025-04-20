from fastapi import APIRouter, FastAPI
from .settings import *
from .funcs import *

router = APIRouter(prefix=prefix, tags=tags)

router.get("/", summary=docs[1]["summary"], description=docs[1]["description"])(get_detail)
router.post("/", summary=docs[2]["summary"], description=docs[2]["description"])(add_detail)
router.delete("/{id}", summary=docs[3]["summary"], description=docs[3]["description"])(delete_detail)
router.put("/{id}", summary=docs[4]["summary"], description=docs[4]["description"])(full_update_detail)
router.patch("/{id}", summary=docs[5]["summary"], description=docs[5]["description"])(part_update_detail)


def add_detail_router(app: FastAPI):
    app.include_router(router)
