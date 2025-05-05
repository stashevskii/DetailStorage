from typing import Optional
from fastapi import HTTPException
from src.app.infrastructure.dependencies import DbDep
from src.app.domain.schemas.user import UserFilter
from src.app.domain.schemas.user import UserPartUpdate
from src.app.domain.schemas.user import UserCreate
from src.app.domain.schemas.user import UserFullUpdate
from src.app.infrastructure.persistence.models.user import User
from src.app.infrastructure.persistence.repositories.user import UserRepository
from src.app.core.utils.exists import raise_exceptions_user_exists, raise_exceptions_user_not_exists
from src.app.core.base.service import Service
from src.app.domain.exceptions.user import NotFoundUserBasicException
from ..interfaces.user import UserServiceInterface


class UserService(Service, UserServiceInterface):
    def __init__(self, session: DbDep):
        super().__init__(UserRepository(session, User))

    def get(self, schema: UserFilter) -> dict[str: list] | HTTPException:
        response = self.repository.get(schema)
        if response == [None] or not response: raise NotFoundUserBasicException

        res_response = []
        for i in response: res_response.append(i.as_dict())

        return {"data": res_response}

    def add(self, schema: UserCreate) -> dict[int: Optional[int], str: bool] | HTTPException:
        raise_exceptions_user_exists(self.repository, schema.id, schema.email)
        new_id = self.repository.add(schema)
        return {"id": new_id, "success": True}

    def delete(self, id: int) -> dict[str: bool] | HTTPException:
        raise_exceptions_user_not_exists(self.repository, id)
        self.repository.delete(id)
        return {"success": True}

    def full_update(self, id, schema: UserFullUpdate) -> dict[int: Optional[int],
                                                                      str: bool] | HTTPException:
        raise_exceptions_user_not_exists(self.repository, id)
        self.repository.full_update(id, schema)
        return {"success": True, "id": id}

    def part_update(self, id, schema: UserPartUpdate) -> dict[int: Optional[int],
                                                                      str: bool] | HTTPException:
        raise_exceptions_user_not_exists(self.repository, id)
        self.repository.part_update(id, schema)
        return {"success": True, "id": id}
