from typing import Optional
from fastapi import HTTPException
from pydantic.v1.schema import schema

from src.app.users.utils.dependencies import DbDep
from src.app.users.schemas.requests.get import GetUserSchemaRequest
from src.app.users.schemas.requests.patch import PartUpdateUserSchemaRequest
from src.app.users.schemas.requests.post import AddUserSchemaRequest, AddUserSchemaRequestWithHashedPassword
from src.app.users.schemas.requests.put import FullUpdateUserSchemaRequest
from src.app.users.models.user import User
from src.app.users.repository.repository import UserRepository
from src.app.users.core.db import Base
from src.app.users.utils.exists import check_user_exist, raise_exceptions_user_exists, raise_exceptions_user_not_exists
from src.app.users.core.common.service import Service
from .interface import UserServiceInterface
from src.app.users.exceptions.business.business import NotFoundUserBasicException, UserAlreadyExistsBasicException
from ..utils.password import hash_password


class UserService(Service, UserServiceInterface):
    def __init__(self, session: DbDep):
        super().__init__(UserRepository(session, User))

    def get(self, schema: GetUserSchemaRequest) -> list[Base]:
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
        return res_response

    def add(self, schema: AddUserSchemaRequest) -> dict[int: Optional[int], str: bool] | HTTPException:
        raise_exceptions_user_exists(self.repository, schema.id, schema.email)
        hashed_password = hash_password(schema.password)
        params = schema.model_dump()
        del params["password"]
        new_id = self.repository.add(AddUserSchemaRequestWithHashedPassword(**params | {"hashed_password": hashed_password}))
        return {"id": new_id, "success": True}

    def delete(self, id: int) -> dict[str: bool] | HTTPException:
        raise_exceptions_user_not_exists(self.repository, id)
        self.repository.delete(id)
        return {"success": True}

    def full_update(self, id, schema: FullUpdateUserSchemaRequest) -> dict[int: Optional[int],
                                                                     str: bool] | HTTPException:
        raise_exceptions_user_not_exists(self.repository, id)
        self.repository.full_update(id, schema)
        return {"success": True, "id": id}

    def part_update(self, id, schema: PartUpdateUserSchemaRequest) -> dict[int: Optional[int],
                                                                     str: bool] | HTTPException:
        raise_exceptions_user_not_exists(self.repository, id)
        update_params = {k: v for k, v in schema.model_dump().items() if v is not None}
        self.repository.part_update(id, update_params)
        return {"success": True, "id": id}
