from fastapi import Depends, APIRouter
from src.app.api.errors import (
    NotFoundUserHttp,
    DuplicateEmailHttp, DuplicateUsernameHttp
)
from src.app.infrastructure.config import config
from src.app.domain.exceptions import (
    NotFoundUserException,
    DuplicateEmailException, DuplicateUsernameException
)
from src.app.domain.schemas import UserPartUpdate, UserSchema, UserFullUpdate, SuccessSchema
from src.app.core.utils import map_exceptions
from src.app.infrastructure.dependencies import UserServiceDep, CurrentUserDep

router = APIRouter(prefix=config.user_router_config.prefix, tags=config.user_router_config.tags)


@router.get(
    "/me",
    summary=config.user_router_config.docs[1]["summary"],
    description=config.user_router_config.docs[1]["description"]
)
def get_current_user(current_user: CurrentUserDep) -> UserSchema:
    return current_user


@router.delete(
    "/me",
    summary=config.user_router_config.docs[2]["summary"],
    description=config.user_router_config.docs[2]["description"]
)
@map_exceptions({NotFoundUserException: NotFoundUserHttp})
def delete_user(service: UserServiceDep, current_user: CurrentUserDep) -> SuccessSchema:
    return service.delete(current_user.id)


@router.put(
    "/me",
    summary=config.user_router_config.docs[3]["summary"],
    description=config.user_router_config.docs[3]["description"]
)
@map_exceptions({
    NotFoundUserException: NotFoundUserHttp,
    DuplicateEmailException: DuplicateEmailHttp,
    DuplicateUsernameException: DuplicateUsernameHttp
})
def replace_user(
        service: UserServiceDep,
        current_user: CurrentUserDep,
        schema: UserFullUpdate = Depends(),
) -> UserSchema:
    return service.replace(current_user.id, schema)


@router.patch(
    "/me",
    summary=config.user_router_config.docs[4]["summary"],
    description=config.user_router_config.docs[4]["description"]
)
@map_exceptions({
    NotFoundUserException: NotFoundUserHttp,
    DuplicateEmailException: DuplicateEmailHttp,
    DuplicateUsernameException: DuplicateUsernameHttp
})
def part_update_user(
        service: UserServiceDep,
        current_user: CurrentUserDep,
        schema: UserPartUpdate = Depends(),
) -> UserSchema:
    return service.part_update(current_user.id, schema)
