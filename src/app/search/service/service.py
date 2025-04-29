from .interface import SearchServiceInterface
from src.app.search.core.common.service import ServiceWithParser
from ..foreign.parser.lego.parser import LegoParser
from ..schemas.lego_id import GetDetailByLegoIdSchema
from ..schemas.name import GetDetailByNameSchema


class SearchService(ServiceWithParser, SearchServiceInterface):
    def __init__(self):
        super().__init__(LegoParser())

    def get_detail_by_lego_id(self, schema: GetDetailByLegoIdSchema):
        return self.parser.get_detail_by_query(schema.lego_id, schema.page_limit)

    def get_detail_by_name(self, schema: GetDetailByNameSchema):
        return self.parser.get_detail_by_query(schema.name, schema.page_limit)
