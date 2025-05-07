from typing import Any
from src.app.domain.exceptions.detail import (
    NotFoundDetailBasicException,
    DetailAlreadyExistsBasicException,
)
from src.app.domain.exceptions.user import (
    UserAlreadyExistsBasicException,
    UserWithThisEmailAlreadyExistsBasicException,
    NotFoundUserBasicException,
    UserWithThisUsernameAlreadyExistsBasicException
)


def exists(repo, **conditions: Any) -> bool:
    return any(all(getattr(obj, key) == value for key, value in conditions.items()) for obj in repo.get_all())


def check_detail_raise_exceptions(
        repo: Any,
        id: int = None,
        check_exists: bool = False,
        check_not_found: bool = False
) -> None:
    if id is not None:
        if check_exists and exists(repo, id=id):
            raise DetailAlreadyExistsBasicException
        if check_not_found and not exists(repo, id=id):
            raise NotFoundDetailBasicException


def check_user_and_raise_exceptions(
        repo: Any,
        id: int = None,
        email: str = None,
        username: str = None,
        check_exists: bool = False,
        check_not_found: bool = False
) -> None:
    if check_exists:
        if id is not None and exists(repo, id=id):
            raise UserAlreadyExistsBasicException
        if email is not None and exists(repo, email=email):
            raise UserWithThisEmailAlreadyExistsBasicException
        if username is not None and exists(repo, username=username):
            raise UserWithThisUsernameAlreadyExistsBasicException

    if check_not_found and id is not None and not exists(repo, id=id):
        raise NotFoundUserBasicException
