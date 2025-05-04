import requests
from bs4 import BeautifulSoup

from src.app.core.common.parser import Parser
from src.app.domain.interfaces.parser import ParserInterface
from src.app.utils.parsing import get_text_from_attribute_list


class LegoParser(Parser, ParserInterface):
    def __init__(self):
        super().__init__("https://www.lego.com/en-us/pick-and-build/pick-a-brick")

    def get_html(self, query: str, page_number: int) -> str:
        response = requests.get(f"{self.url}?query={query}&page={page_number}")
        return response.text

    def get_detail_by_query(self, q: str, pq: int) -> dict:
        if not q:
            return {"data": []}
        res = []

        for i in range(pq):
            soup = BeautifulSoup(self.get_html(str(q), i), "html.parser")
            ids = get_text_from_attribute_list(soup.find_all(class_="ElementLeaf_elementId__Ivgn4 ds-body-xs-regular"))
            for j in range(len(ids)):
                ids[j] = ids[j].split("/")[0][4:]
            names = get_text_from_attribute_list(
                soup.find_all(class_="ElementLeaf_elementTitle__SwFh1 ds-body-sm-regular"))
            res += [{"id": a, "name": b} for a, b in zip(ids, names)]

        return {"data": res} if res else {}
