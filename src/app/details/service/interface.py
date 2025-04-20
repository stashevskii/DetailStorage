from abc import abstractmethod, ABC
from typing import Optional
from fastapi import HTTPException
from src.app.bases.base_model import Base
from src.app.details.schemas.requests.get import GetDetailSchemaRequest
from src.app.details.schemas.requests.patch import PartUpdateDetailSchemaRequest
from src.app.details.schemas.requests.post import AddDetailSchemaRequest
from src.app.details.schemas.requests.put import FullUpdateDetailSchemaRequest
from src.app.details.schemas.responses.delete import DeleteDetailSchemaResponse


class DetailServiceInterface(ABC):
    @abstractmethod
    def get_detail(self, gds: GetDetailSchemaRequest) -> list[Base]:
        raise NotImplemented

    @abstractmethod
    def add_detail(self, ads: AddDetailSchemaRequest) -> dict[int: Optional[int], str: bool] | HTTPException:
        raise NotImplemented

    @abstractmethod
    def delete_detail(self, id: int) -> dict[str: bool] | HTTPException:
        raise NotImplemented

    @abstractmethod
    def full_update_detail(self, id, uds: FullUpdateDetailSchemaRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        raise NotImplemented

    @abstractmethod
    def part_update_detail(self, id, uds: PartUpdateDetailSchemaRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        raise NotImplemented