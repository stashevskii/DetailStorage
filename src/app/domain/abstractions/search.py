from abc import ABC, abstractmethod


class SearchServiceInterface(ABC):
    @abstractmethod
    def get_detail_by_lego_id(self, schema):
        raise NotImplemented

    @abstractmethod
    def get_detail_by_name(self, schema):
        raise NotImplemented


class LegoParserInterface(ABC):
    @abstractmethod
    def get_html(self, query, page_number):
        raise NotImplemented
