from typing import Any

from pydantic import EmailStr

from src.app.domain.exceptions import (
    UserAlreadyExistsException,
    DuplicateEmailException,
    NotFoundUserException,
    DuplicateUsernameException,
    NotFoundDetailException,
    DetailAlreadyExistsException,
)


def exists(repo, **conditions) -> bool:
    return any(all(getattr(obj, key) == value for key, value in conditions.items()) for obj in repo.get_all())


def check_detail_raise_exceptions(
        repo,
        id: int = None,
        check_exists: bool = False,
        check_not_found: bool = False
) -> None:
    if id is not None:
        if check_exists and exists(repo, id=id):
            raise DetailAlreadyExistsException
        if check_not_found and not exists(repo, id=id):
            raise NotFoundDetailException


def check_user_and_raise_exceptions(
        repo,
        id: int = None,
        email: str | EmailStr = None,
        username: str = None,
        check_exists: bool = False,
        check_not_found: bool = False
) -> None:
    if check_exists:
        if id is not None and exists(repo, id=id):
            raise UserAlreadyExistsException
        if email is not None and exists(repo, email=email):
            raise DuplicateEmailException
        if username is not None and exists(repo, username=username):
            raise DuplicateUsernameException

    if check_not_found and id is not None and not exists(repo, id=id):
        raise NotFoundUserException


def check_user_owns_detail_and_raise_exceptions(repo, detail_id: int, user_id: int) -> None:
    if not any(detail.id == detail_id for detail in repo.get_by_id(user_id).details):
        raise NotFoundDetailException
