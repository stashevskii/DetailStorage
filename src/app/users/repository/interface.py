from src.app.users.schemas.requests.post import AddUserSchemaRequest
from src.app.users.schemas.requests.put import FullUpdateUserSchemaRequest
from abc import abstractmethod, ABC


class UserRepositoryInterface(ABC):
    @abstractmethod
    def get(self, filter_params: dict, all_obj: bool) -> dict:
        raise NotImplemented

    @abstractmethod
    def add(self, ads: AddUserSchemaRequest) -> int:
        raise NotImplemented

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplemented

    @abstractmethod
    def full_update(self, id: int, uds: FullUpdateUserSchemaRequest) -> None:
        raise NotImplemented

    @abstractmethod
    def part_update(self, id: int, update_params: dict) -> None:
        raise NotImplemented
