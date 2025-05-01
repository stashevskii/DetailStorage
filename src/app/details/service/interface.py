from abc import abstractmethod, ABC
from typing import Optional
from fastapi import HTTPException
from src.app.details.core.db import Base
from src.app.details.schemas.requests.get import GetDetailSchemaRequest
from src.app.details.schemas.requests.patch import PartUpdateDetailSchemaRequest
from src.app.details.schemas.requests.post import AddDetailSchemaRequest
from src.app.details.schemas.requests.put import FullUpdateDetailSchemaRequest


class DetailServiceInterface(ABC):
    @abstractmethod
    def get(self, schema: GetDetailSchemaRequest) -> list[Base]:
        raise NotImplemented

    @abstractmethod
    def add(self, schema: AddDetailSchemaRequest) -> dict[int: Optional[int], str: bool] | HTTPException:
        raise NotImplemented

    @abstractmethod
    def delete(self, id: int) -> dict[str: bool] | HTTPException:
        raise NotImplemented

    @abstractmethod
    def full_update(self, id, schema: FullUpdateDetailSchemaRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        raise NotImplemented

    @abstractmethod
    def part_update(self, id, schema: PartUpdateDetailSchemaRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        raise NotImplemented