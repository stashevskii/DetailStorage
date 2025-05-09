import requests
from bs4 import BeautifulSoup
from src.app.core.base.parser import Parser
from src.app.domain.abstractions.search import LegoParserInterface
from src.app.core.utils.parsing import get_text_from_attribute_list
from src.app.infrastructure.web.logger import get_logger

log = get_logger(__name__)


class LegoParser(Parser, LegoParserInterface):
    def __init__(self):
        super().__init__("https://www.lego.com/en-us/pick-and-build/pick-a-brick")

    def get_html(self, query: str, page_number: int) -> str:
        url = f"{self.url}?query={query}&page={page_number}"
        log.info("Send get request to %s", url)
        response = requests.get(url)
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
                soup.find_all(class_="ElementLeaf_elementTitle__SwFh1 ds-body-sm-regular")
            )
            res += [{"id": a, "name": b} for a, b in zip(ids, names)]

        return {"data": res} if res else {}
