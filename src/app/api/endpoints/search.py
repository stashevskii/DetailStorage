from fastapi import APIRouter
from fastapi.params import Depends
from src.app.infrastructure.config.main import config
from src.app.domain.schemas.search import DetailLegoId
from src.app.domain.schemas.search import DetailName
from src.app.domain.services.search import SearchService

router = APIRouter(prefix=config.search_router_config.prefix, tags=config.search_router_config.tags)


@router.get(
    "/get-detail-by-lego-id",
    summary=config.search_router_config.docs[1]["summary"],
    description=config.search_router_config.docs[1]["description"]
)
def get_detail_by_lego_id(schema: DetailLegoId = Depends(), service: SearchService = Depends(SearchService)):
    return service.get_detail_by_lego_id(schema)


@router.get(
    "/get-detail-by-name",
    summary=config.search_router_config.docs[2]["summary"],
    description=config.search_router_config.docs[2]["description"]
)
def get_detail_by_name(schema: DetailName = Depends(), service: SearchService = Depends(SearchService)):
    return service.get_detail_by_name(schema)
