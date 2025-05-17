from fastapi import APIRouter, Depends
from src.app.api.errors import NotFoundUserHttp, DuplicateEmailHttp, DuplicateUsernameHttp
from src.app.core.utils import map_exceptions
from src.app.domain.exceptions import NotFoundUserException, UserAlreadyExistsException, DuplicateEmailException, \
    DuplicateUsernameException
from src.app.domain.schemas import UserCreate, UserSchema, SuccessSchema, UserFullUpdate, UserPartUpdate
from src.app.infrastructure.config import config
from src.app.infrastructure.dependencies import AdminServiceDep

router = APIRouter(prefix=config.admin_router_config.prefix, tags=config.admin_router_config.tags)


@router.get(
    "/users/all",
)
@map_exceptions({NotFoundUserException: NotFoundUserHttp})
def get_all_users(
        service: AdminServiceDep
) -> list[UserSchema]:
    return service.get_all()


@router.post(
    "/users",
)
@map_exceptions({
    UserAlreadyExistsException: UserAlreadyExistsException,
    DuplicateEmailException: DuplicateEmailHttp,
    DuplicateUsernameException: DuplicateUsernameHttp,
})
def add_user(
        service: AdminServiceDep,
        schema: UserCreate = Depends()
) -> UserSchema:
    return service.add(schema)


@router.delete(
    "/users/{id}",
)
@map_exceptions({NotFoundUserException: NotFoundUserHttp})
def delete_user(
        id: int,
        service: AdminServiceDep,
) -> SuccessSchema:
    return service.delete(id)


@router.put(
    "/users/{id}",
)
@map_exceptions({
    NotFoundUserException: NotFoundUserHttp,
    DuplicateUsernameException: DuplicateUsernameHttp,
    DuplicateEmailException: DuplicateEmailHttp,
})
def replace_user(
        id: int,
        service: AdminServiceDep,
        schema: UserPartUpdate = Depends()
) -> UserSchema:
    return service.replace(id, schema)


@router.patch(
    "/users/{id}",
)
@map_exceptions({
    NotFoundUserException: NotFoundUserHttp,
    DuplicateUsernameException: DuplicateUsernameHttp,
    DuplicateEmailException: DuplicateEmailHttp,
})
def replace_user(
        id: int,
        service: AdminServiceDep,
        schema: UserPartUpdate = Depends(),
) -> UserSchema:
    return service.part_update(id, schema)
