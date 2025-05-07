from typing import Optional
from fastapi import HTTPException
from src.app.domain.schemas.user import UserFilter
from src.app.domain.schemas.user import UserPartUpdate
from src.app.domain.schemas.user import UserCreate
from src.app.domain.schemas.user import UserFullUpdate
from src.app.core.utils.exists import check_user_and_raise_exceptions
from src.app.core.base.service import Service
from src.app.domain.exceptions.user import NotFoundUserBasicException
from ..interfaces.user import UserServiceInterface, UserRepositoryInterface


class UserService(Service, UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        super().__init__(user_repository)

    def get(self, schema: UserFilter) -> dict[str: list] | HTTPException:
        response = self.repository.get(schema)
        if response == [None] or not response: raise NotFoundUserBasicException

        res_response = []
        for i in response: res_response.append(i.as_dict())

        return {"data": res_response}

    def add(self, schema: UserCreate) -> dict[int: Optional[int], str: bool] | HTTPException:
        check_user_and_raise_exceptions(self.repository, schema.id, schema.email, schema.username, check_exists=True)
        new_id = self.repository.add(schema)
        return {"id": new_id, "success": True}

    def delete(self, id: int) -> dict[str: bool] | HTTPException:
        check_user_and_raise_exceptions(self.repository, id, check_not_found=True)
        self.repository.delete(id)
        return {"success": True}

    def full_update(self, id, schema: UserFullUpdate) -> dict[int: Optional[int], str: bool] | HTTPException:
        check_user_and_raise_exceptions(self.repository, id, check_not_found=True)
        check_user_and_raise_exceptions(
            self.repository,
            email=schema.email,
            username=schema.username,
            check_exists=True
        )
        self.repository.full_update(id, schema)
        return {"success": True, "id": id}

    def part_update(self, id, schema: UserPartUpdate) -> dict[int: Optional[int], str: bool] | HTTPException:
        check_user_and_raise_exceptions(self.repository, id, check_not_found=True)
        check_user_and_raise_exceptions(
            self.repository,
            email=schema.email,
            username=schema.username,
            check_exists=True
        )
        self.repository.part_update(id, schema)
        return {"success": True, "id": id}
