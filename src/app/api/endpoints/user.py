from typing import Dict

from fastapi import Depends, APIRouter
from src.app.api.errors.http.user import (
    NotFoundUserHttpException,
    UserAlreadyExistsHttpException,
    UserWithThisEmailAlreadyExistsHttpException
)
from src.app.core.config import config
from src.app.core.shared.schemas import BaseResponseSchema, SuccessSchema
from src.app.domain.exceptions.user import (
    NotFoundUserBasicException,
    UserAlreadyExistsBasicException,
    UserWithThisEmailAlreadyExistsBasicException
)
from src.app.domain.schemas.user import UserFilter
from src.app.domain.schemas.user import UserPartUpdate
from src.app.domain.schemas.user import UserCreate
from src.app.domain.schemas.user import UserFullUpdate
from src.app.domain.schemas.user import UserSchema
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
             schema: UserFilter = Depends()) -> Dict[str, list[UserSchema]]:
    return service.get(schema)


@router.post(
    "/",
    summary=config.user_router_config.docs[2]["summary"],
    description=config.user_router_config.docs[2]["description"]
)
@map_exceptions((UserAlreadyExistsBasicException, UserWithThisEmailAlreadyExistsBasicException),
                (UserAlreadyExistsHttpException, UserWithThisEmailAlreadyExistsHttpException))
def add_user(service: UserService = Depends(UserService),
             schema: UserCreate = Depends()) -> BaseResponseSchema:
    return service.add(schema)


@router.delete(
    "/{id}",
    summary=config.user_router_config.docs[3]["summary"],
    description=config.user_router_config.docs[3]["description"]
)
@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def delete_user(id: int, service: UserService = Depends(UserService)) -> SuccessSchema:
    return service.delete(id)


@router.put(
    "/{id}",
    summary=config.user_router_config.docs[4]["summary"],
    description=config.user_router_config.docs[4]["description"]
)
@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def full_update_user(id: int, service: UserService = Depends(UserService),
                     schema: UserFullUpdate = Depends()) -> BaseResponseSchema:
    return service.full_update(id, schema)


@router.patch(
    "/{id}",
    summary=config.user_router_config.docs[5]["summary"],
    description=config.user_router_config.docs[5]["description"]
)
@map_exceptions((NotFoundUserBasicException,), (NotFoundUserHttpException,))
def part_update_user(id: int, service: UserService = Depends(UserService),
                     schema: UserPartUpdate = Depends()) -> BaseResponseSchema:
    return service.part_update(id, schema)
