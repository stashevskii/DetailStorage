from typing import Dict

from fastapi import Depends, APIRouter
from src.app.api.errors.http.user import (
    NotFoundUserHttpException,
    UserAlreadyExistsHttpException,
    UserWithThisEmailAlreadyExistsHttpException, UserWithThisUsernameAlreadyExistsHttpException
)
from src.app.infrastructure.config.main import config
from src.app.domain.schemas.shared import BaseResponseSchema, SuccessSchema
from src.app.domain.exceptions.user import (
    NotFoundUserBasicException,
    UserAlreadyExistsBasicException,
    UserWithThisEmailAlreadyExistsBasicException, UserWithThisUsernameAlreadyExistsBasicException
)
from src.app.domain.schemas.user import UserFilter
from src.app.domain.schemas.user import UserPartUpdate
from src.app.domain.schemas.user import UserCreate
from src.app.domain.schemas.user import UserFullUpdate
from src.app.domain.schemas.user import UserSchema
from src.app.core.utils.decorators import map_exceptions
from src.app.infrastructure.dependencies import UserServiceDep

router = APIRouter(prefix=config.user_router_config.prefix, tags=config.user_router_config.tags)


@router.get(
    "/",
    summary=config.user_router_config.docs[1]["summary"],
    description=config.user_router_config.docs[1]["description"]
)
@map_exceptions({NotFoundUserBasicException: NotFoundUserHttpException})
def get_user(service: UserServiceDep,
             schema: UserFilter = Depends()) -> Dict[str, list[UserSchema]]:
    return service.get(schema)


@router.post(
    "/",
    summary=config.user_router_config.docs[2]["summary"],
    description=config.user_router_config.docs[2]["description"]
)
@map_exceptions({
    UserAlreadyExistsBasicException: UserAlreadyExistsHttpException,
    UserWithThisEmailAlreadyExistsBasicException: UserWithThisUsernameAlreadyExistsHttpException,
    UserWithThisUsernameAlreadyExistsBasicException: UserWithThisUsernameAlreadyExistsHttpException
})
def add_user(service: UserServiceDep,
             schema: UserCreate = Depends()) -> BaseResponseSchema:
    return service.add(schema)


@router.delete(
    "/{id}",
    summary=config.user_router_config.docs[3]["summary"],
    description=config.user_router_config.docs[3]["description"]
)
@map_exceptions({NotFoundUserBasicException: NotFoundUserHttpException})
def delete_user(id: int, service: UserServiceDep) -> SuccessSchema:
    return service.delete(id)


@router.put(
    "/{id}",
    summary=config.user_router_config.docs[4]["summary"],
    description=config.user_router_config.docs[4]["description"]
)
@map_exceptions({
    NotFoundUserBasicException: NotFoundUserHttpException,
    UserWithThisEmailAlreadyExistsBasicException: UserWithThisEmailAlreadyExistsHttpException,
    UserWithThisUsernameAlreadyExistsBasicException: UserWithThisUsernameAlreadyExistsHttpException
})
def full_update_user(id: int, service: UserServiceDep,
                     schema: UserFullUpdate = Depends()) -> BaseResponseSchema:
    return service.full_update(id, schema)


@router.patch(
    "/{id}",
    summary=config.user_router_config.docs[5]["summary"],
    description=config.user_router_config.docs[5]["description"]
)
@map_exceptions({
    NotFoundUserBasicException: NotFoundUserHttpException,
    UserWithThisEmailAlreadyExistsBasicException: UserWithThisEmailAlreadyExistsHttpException,
    UserWithThisUsernameAlreadyExistsBasicException: UserWithThisUsernameAlreadyExistsHttpException
})
def part_update_user(id: int, service: UserServiceDep,
                     schema: UserPartUpdate = Depends()) -> BaseResponseSchema:
    return service.part_update(id, schema)
