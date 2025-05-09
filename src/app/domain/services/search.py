from src.app.domain.abstractions.search import SearchServiceInterface, LegoParserInterface
from src.app.core.base import ParserService
from src.app.domain.schemas import DetailLegoId, DetailName


class SearchService(ParserService, SearchServiceInterface):
    def __init__(self, lego_parser: LegoParserInterface):
        super().__init__(lego_parser)

    def get_detail_by_lego_id(self, schema: DetailLegoId):
        return self.parser.get_detail_by_query(schema.lego_id, schema.page_limit)

    def get_detail_by_name(self, schema: DetailName):
        return self.parser.get_detail_by_query(schema.name, schema.page_limit)
