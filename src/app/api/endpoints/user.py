from typing import Dict

from fastapi import Depends, APIRouter
from src.app.api.errors.http.user import (
    NotFoundUserHttpException,
    UserAlreadyExistsHttpException,
    UserWithThisEmailAlreadyExistsHttpException
)
from src.app.core.config import config
from src.app.domain.exceptions.user import (
    NotFoundUserBasicException,
    UserAlreadyExistsBasicException,
    UserWithThisEmailAlreadyExistsBasicException
)
from src.app.domain.schemas.user.requests.get import GetUserSchemaRequest
from src.app.domain.schemas.user.requests.patch import PartUpdateUserSchemaRequest
from src.app.domain.schemas.user.requests.post import AddUserSchemaRequest
from src.app.domain.schemas.user.requests.put import FullUpdateUserSchemaRequest
from src.app.domain.schemas.user.responses.delete import DeleteUserSchemaResponse
from src.app.domain.schemas.user.responses.get import GetUserSchemaResponse
from src.app.domain.schemas.user.responses.patch import PartUpdateUserSchemaResponse
from src.app.domain.schemas.user.responses.post import AddUserSchemaResponse
from src.app.domain.schemas.user.responses.put import FullUpdateUserSchemaResponse
from src.app.domain.services.user import UserService
from src.app.utils.decorators import map_exceptions

router = APIRouter(prefix=config.user_router_config.prefix, tags=config.user_router_config.tags)


@router.get(
    "/",
    summary=config.user_router_config.docs[1]["summary"],
    description=config.user_router_config.docs[1]["description"]
)
@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def get_user(service: UserService = Depends(UserService),
             schema: GetUserSchemaRequest = Depends()) -> Dict[str, list[GetUserSchemaResponse]]:
    return service.get(schema)


@router.post(
    "/",
    summary=config.user_router_config.docs[2]["summary"],
    description=config.user_router_config.docs[2]["description"]
)
@map_exceptions((UserAlreadyExistsBasicException, UserWithThisEmailAlreadyExistsBasicException),
                (UserAlreadyExistsHttpException, UserWithThisEmailAlreadyExistsHttpException))
def add_user(service: UserService = Depends(UserService),
             schema: AddUserSchemaRequest = Depends()) -> AddUserSchemaResponse:
    return service.add(schema)


@router.delete(
    "/",
    summary=config.user_router_config.docs[3]["summary"],
    description=config.user_router_config.docs[3]["description"]
)
@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def delete_user(id: int, service: UserService = Depends(UserService)) -> DeleteUserSchemaResponse:
    return service.delete(id)


@router.put(
    "/",
    summary=config.user_router_config.docs[4]["summary"],
    description=config.user_router_config.docs[4]["description"]
)
@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def full_update_user(id: int, service: UserService = Depends(UserService),
                     schema: FullUpdateUserSchemaRequest = Depends()) -> FullUpdateUserSchemaResponse:
    return service.full_update(id, schema)


@router.patch(
    "/",
    summary=config.user_router_config.docs[5]["summary"],
    description=config.user_router_config.docs[5]["description"]
)
@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def part_update_user(id: int, service: UserService = Depends(UserService),
                     schema: PartUpdateUserSchemaRequest = Depends()) -> PartUpdateUserSchemaResponse:
    return service.part_update(id, schema)
