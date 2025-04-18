from fastapi import APIRouter, FastAPI
from .settings import *
from .views import *

router = APIRouter(prefix=prefix, tags=tags)

router.get("/", summary="Get detail by parameters", description="Get detail by parameters endpoint")(get_detail)
router.post("/", summary="Add new detail", description="Add new detail endpoint")(add_detail)
router.delete("/{id}", summary="Delete detail", description="Delete detail endpoint")(delete_detail)
router.put("/{id}", summary="Full update detail", description="Full update detail endpoint")(full_update_detail)
router.patch("/{id}", summary="Part update detail", description="Part update detail endpoint")(part_update_detail)


def add_detail_router(app: FastAPI):
    app.include_router(router)
