from src.app.users.exceptions.business.business import (
    UserWithThisEmailAlreadyExistsBasicException,
    UserAlreadyExistsBasicException,
    NotFoundUserBasicException
)
from src.app.users.repository.repository import UserRepository


def check_user_exist(repo: UserRepository, id: int) -> bool:
    if id is None:
        return False

    all_users = repo.get_all()
    for i in all_users:
        if i.id == id:
            return True
    return False


def check_user_exist_by_email(repo: UserRepository, email: str) -> bool:
    if email is None:
        return False

    all_users = repo.get_all()
    for i in all_users:
        if i.email == email:
            return True
    return False


def raise_exceptions_user_exists(
    repo: UserRepository,
    id: int,
    email: str,
):
    if check_user_exist(repo, id):
        raise UserAlreadyExistsBasicException
    elif check_user_exist_by_email(repo, email):
        raise UserWithThisEmailAlreadyExistsBasicException

def raise_exceptions_user_not_exists(
    repo: UserRepository,
    id: int,
):
    if not check_user_exist(repo, id):
        raise NotFoundUserBasicException
