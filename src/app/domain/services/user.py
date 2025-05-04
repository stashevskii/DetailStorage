from typing import Optional
from fastapi import HTTPException
from src.app.utils.dependencies import DbDep
from src.app.domain.schemas.user import UserFilter
from src.app.domain.schemas.user import UserPartUpdate
from src.app.domain.schemas.user import UserCreate
from src.app.domain.schemas.user import UserFullUpdate
from src.app.domain.models.user import User
from src.app.repositories.user import UserRepository
from src.app.utils.exists import raise_exceptions_user_exists, raise_exceptions_user_not_exists
from src.app.core.common.service import Service
from src.app.domain.exceptions.user import NotFoundUserBasicException
from src.app.utils.password import hash_password
from ..interfaces.user import UserServiceInterface


class UserService(Service, UserServiceInterface):
    def __init__(self, session: DbDep):
        super().__init__(UserRepository(session, User))

    def get(self, schema: UserFilter) -> dict[str: list] | HTTPException:
        get_params = {}
        for k, v in schema.model_dump().items():
            if v is not None:
                get_params[k] = v

        del get_params["all_obj"]
        response = self.repository.get(get_params, schema.all_obj)
        if response == [None] or not response:
            raise NotFoundUserBasicException

        res_response = []

        for i in response:
            res_response.append(i.as_dict())
        return {"data": res_response}

    def add(self, schema: UserCreate) -> dict[int: Optional[int], str: bool] | HTTPException:
        raise_exceptions_user_exists(self.repository, schema.id, schema.email)
        hashed_password = hash_password(schema.password)
        params = schema.model_dump()
        del params["password"]
        new_id = self.repository.add(params | {"hashed_password": hashed_password})
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
        update_params = {k: v for k, v in schema.model_dump().items() if v is not None}
        self.repository.part_update(id, update_params)
        return {"success": True, "id": id}
