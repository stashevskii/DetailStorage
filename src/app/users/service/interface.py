from abc import abstractmethod, ABC
from typing import Optional
from fastapi import HTTPException
from src.app.users.core.db import Base
from src.app.users.schemas.requests.get import GetUserSchemaRequest
from src.app.users.schemas.requests.patch import PartUpdateUserSchemaRequest
from src.app.users.schemas.requests.post import AddUserSchemaRequest
from src.app.users.schemas.requests.put import FullUpdateUserSchemaRequest


class UserServiceInterface(ABC):
    @abstractmethod
    def get(self, gds: GetUserSchemaRequest) -> list[Base]:
        raise NotImplemented

    @abstractmethod
    def add(self, ads: AddUserSchemaRequest) -> dict[int: Optional[int], str: bool] | HTTPException:
        raise NotImplemented

    @abstractmethod
    def delete(self, id: int) -> dict[str: bool] | HTTPException:
        raise NotImplemented

    @abstractmethod
    def full_update(self, id, uds: FullUpdateUserSchemaRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        raise NotImplemented

    @abstractmethod
    def part_update(self, id, uds: PartUpdateUserSchemaRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        raise NotImplemented