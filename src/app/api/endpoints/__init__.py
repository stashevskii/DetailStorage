from fastapi import APIRouter, FastAPI
from .detail import router as detail_router
from .search import router as search_router
from .user import router as user_router

router = APIRouter()
router.include_router(detail_router)
router.include_router(search_router)
router.include_router(user_router)


def include_main_router(app: FastAPI) -> None:
    app.include_router(router)


__all__ = ["include_main_router"]
