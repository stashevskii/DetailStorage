from src.app.domain.interfaces.search import SearchServiceInterface
from src.app.core.base.service import ServiceWithParser
from src.app.infrastructure.external.lego_parser import LegoParser
from src.app.domain.schemas.search import DetailLegoId
from src.app.domain.schemas.search import DetailName


class SearchService(ServiceWithParser, SearchServiceInterface):
    def __init__(self):
        super().__init__(LegoParser())

    def get_detail_by_lego_id(self, schema: DetailLegoId):
        return self.parser.get_detail_by_query(schema.lego_id, schema.page_limit)

    def get_detail_by_name(self, schema: DetailName):
        return self.parser.get_detail_by_query(schema.name, schema.page_limit)
