from fastapi import Depends, HTTPException
from src.app.users.exceptions.http.http import (
    NotFoundUserHttpException,
    UserAlreadyExistsHttpException,
    UserWithThisEmailAlreadyExistsHttpException
)
from src.app.users.exceptions.business.business import (
    NotFoundUserBasicException,
    UserAlreadyExistsBasicException,
    UserWithThisEmailAlreadyExistsBasicException
)
from src.app.users.schemas.requests.get import GetUserSchemaRequest
from src.app.users.schemas.requests.patch import PartUpdateUserSchemaRequest
from src.app.users.schemas.requests.post import AddUserSchemaRequest
from src.app.users.schemas.requests.put import FullUpdateUserSchemaRequest
from src.app.users.schemas.responses.delete import DeleteUserSchemaResponse
from src.app.users.schemas.responses.get import GetUserSchemaResponse
from src.app.users.schemas.responses.patch import PartUpdateUserSchemaResponse
from src.app.users.schemas.responses.post import AddUserSchemaResponse
from src.app.users.schemas.responses.put import FullUpdateUserSchemaResponse
from src.app.users.service.service import UserService
from src.app.users.utils.decorators import map_exceptions


@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def get_user(service: UserService = Depends(UserService),
             schema: GetUserSchemaRequest = Depends()) -> list[GetUserSchemaResponse]:
    return service.get(schema)


@map_exceptions((UserAlreadyExistsBasicException, UserWithThisEmailAlreadyExistsBasicException),
                (UserAlreadyExistsHttpException, UserWithThisEmailAlreadyExistsHttpException))
def add_user(service: UserService = Depends(UserService),
             schema: AddUserSchemaRequest = Depends()) -> AddUserSchemaResponse:
    return service.add(schema)


@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def delete_user(id: int, service: UserService = Depends(UserService)) -> DeleteUserSchemaResponse:
    return service.delete(id)


@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def full_update_user(id: int, service: UserService = Depends(UserService),
                     schema: FullUpdateUserSchemaRequest = Depends()) -> FullUpdateUserSchemaResponse:
    return service.full_update(id, schema)


@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def part_update_user(id: int, service: UserService = Depends(UserService),
                     schema: PartUpdateUserSchemaRequest = Depends()) -> PartUpdateUserSchemaResponse:
    return service.part_update(id, schema)
