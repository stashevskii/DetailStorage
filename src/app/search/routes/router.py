from fastapi import APIRouter
from .funcs import *
from src.app.search.config.config import router_config

router = APIRouter(
    prefix=router_config.prefix,
    tags=router_config.tags,
)

router.get("/get-detail-by-lego-id")(get_detail_by_lego_id)
router.get("/get-detail-by-name")(get_detail_by_name)
