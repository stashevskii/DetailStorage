from typing import Annotated
from fastapi import Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from sqlalchemy.orm import Session

from src.app.api.errors import InvalidPasswordOrUsernameHttpError
from src.app.api.errors.auth import UnauthedHttpError
from src.app.core.utils import compare_passwords
from src.app.core.utils.password import get_bytes_from_db_hex_hash
from src.app.domain.services import DetailService, SearchService, UserService
from src.app.domain.services.auth import AuthService
from src.app.infrastructure.external import LegoParser
from src.app.infrastructure.persistence.db import get_db
from src.app.infrastructure.persistence.models import User
from src.app.infrastructure.persistence.repositories.detail import DetailRepository
from src.app.infrastructure.persistence.repositories.user import UserRepository

DbDep = Annotated[Session, Depends(get_db)]


def get_detail_repo(db: DbDep):
    return DetailRepository(db)


def get_user_repo(db: DbDep):
    return UserRepository(db)


UserRepositoryDep = Annotated[UserRepository, Depends(get_user_repo)]
DetailRepositoryDep = Annotated[DetailRepository, Depends(get_detail_repo)]


def get_detail_service(detail_repository: DetailRepositoryDep, user_repository: UserRepositoryDep):
    return DetailService(detail_repository, user_repository)


def get_user_service(user_repository: UserRepositoryDep, detail_repository: DetailRepositoryDep):
    return UserService(user_repository, detail_repository)


def get_search_service():
    return SearchService(LegoParser())


def get_auth_service(user_repository: UserRepositoryDep):
    return AuthService(user_repository)


DetailServiceDep = Annotated[DetailService, Depends(get_detail_service)]
UserServiceDep = Annotated[UserService, Depends(get_user_service)]
SearchServiceDep = Annotated[SearchService, Depends(get_search_service)]
AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]
CredentialsDep = Annotated[HTTPBasicCredentials, Depends(HTTPBasic())]


def get_current_user(
        credentials: Annotated[HTTPBasicCredentials, Depends(HTTPBasic(auto_error=False))],
        user_repository=Depends(get_user_repo)
) -> User:
    if credentials is None:
        raise UnauthedHttpError
    user = user_repository.get_by_username(credentials.username)
    if not user or not compare_passwords(credentials.password, get_bytes_from_db_hex_hash(user.hashed_password)):
        raise UnauthedHttpError
    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]
