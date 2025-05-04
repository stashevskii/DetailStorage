from typing import Any
from src.app.domain.exceptions.detail import (
    NotFoundDetailBasicException,
    DetailAlreadyExistsBasicException,
)
from src.app.domain.exceptions.user import (
    UserAlreadyExistsBasicException,
    UserWithThisEmailAlreadyExistsBasicException,
    NotFoundUserBasicException
)
from src.app.infrastructure.persistence.repositories.detail import DetailRepository
from src.app.infrastructure.persistence.repositories.user import UserRepository


def exists(repo, param_name: str, value: Any) -> bool:
    return value is not None and any(
        getattr(obj, param_name) == value for obj in repo.get_all()
    )


def check_detail_exist(repo: DetailRepository, id: int) -> bool:
    return exists(repo, "id", id)


def check_user_exist(repo: UserRepository, id: int) -> bool:
    return exists(repo, "id", id)


def check_user_exist_by_email(repo: UserRepository, email: str) -> bool:
    return exists(repo, "email", email)


def raise_exceptions_detail_not_found(repo: DetailRepository, id: int):
    if not check_detail_exist(repo, id): raise NotFoundDetailBasicException


def raise_exceptions_adding_detail(repo: DetailRepository, detail_id: int):
    if check_detail_exist(repo, detail_id): raise DetailAlreadyExistsBasicException


def raise_exceptions_user_exists(repo: UserRepository, id: int, email: str):
    if check_user_exist(repo, id):
        raise UserAlreadyExistsBasicException
    elif check_user_exist_by_email(repo, email):
        raise UserWithThisEmailAlreadyExistsBasicException


def raise_exceptions_user_not_exists(repo: UserRepository, id: int):
    if not check_user_exist(repo, id): raise NotFoundUserBasicException
