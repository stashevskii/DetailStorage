from abc import ABC, abstractmethod


class ParserInterface(ABC):
    @abstractmethod
    def get_html(self, query, page_number):
        raise NotImplemented
