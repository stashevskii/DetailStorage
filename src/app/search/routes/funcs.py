from fastapi.params import Depends
from src.app.search.schemas.lego_id import GetDetailByLegoIdSchema
from src.app.search.schemas.name import GetDetailByNameSchema
from src.app.search.service.service import SearchService


def get_detail_by_lego_id(schema: GetDetailByLegoIdSchema = Depends(), service: SearchService = Depends(SearchService)):
    return service.get_detail_by_lego_id(schema)


def get_detail_by_name(schema: GetDetailByNameSchema = Depends(), service: SearchService = Depends(SearchService)):
    return service.get_detail_by_name(schema)
