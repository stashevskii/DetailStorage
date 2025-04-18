from src.app.entities.details.requests.post import AddDetailSchemaRequest
from src.app.entities.details.requests.put import FullUpdateDetailSchemaRequest
from abc import abstractmethod, ABC


class DetailInterface(ABC):
    @abstractmethod
    def get(self, filter_params: dict, all_obj: bool) -> dict:
        raise NotImplemented

    @abstractmethod
    def add(self, ads: AddDetailSchemaRequest) -> int:
        raise NotImplemented

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplemented

    @abstractmethod
    def full_update(self, id: int, uds: FullUpdateDetailSchemaRequest) -> None:
        raise NotImplemented

    @abstractmethod
    def part_update(self, id: int, update_params: dict) -> None:
        raise NotImplemented
