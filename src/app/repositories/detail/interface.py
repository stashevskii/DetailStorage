from src.app.dtos.detail.requests.post import AddDetailDtoRequest
from src.app.dtos.detail.requests.put import FullUpdateDetailDtoRequest
from abc import abstractmethod, ABC


class DetailInterface(ABC):
    @abstractmethod
    def get(self, filter_params: dict, all_obj: bool) -> dict:
        raise NotImplemented

    @abstractmethod
    def add(self, ads: AddDetailDtoRequest) -> int:
        raise NotImplemented

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplemented

    @abstractmethod
    def full_update(self, id: int, uds: FullUpdateDetailDtoRequest) -> None:
        raise NotImplemented

    @abstractmethod
    def part_update(self, id: int, update_params: dict) -> None:
        raise NotImplemented
