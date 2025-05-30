from typing import Annotated
from fastapi import Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from sqlalchemy.orm import Session
from src.app.api.errors.auth import UnauthedHttp
from src.app.core.utils import compare_passwords
from src.app.core.utils.password import get_bytes_from_db_hex_hash
from src.app.domain.abstractions import DetailRepositoryInterface, UserRepositoryInterface, DetailServiceInterface, \
    UserServiceInterface, SearchServiceInterface
from src.app.domain.abstractions.auth import AuthServiceInterface
from src.app.domain.services import DetailService, SearchService, UserService
from src.app.domain.services.admin import AdminService
from src.app.domain.services.auth import AuthService
from src.app.infrastructure.external import LegoParser
from src.app.infrastructure.persistence.db import get_db
from src.app.infrastructure.persistence.models import User
from src.app.infrastructure.persistence.repositories.detail import DetailRepository
from src.app.infrastructure.persistence.repositories.user import UserRepository

DbDep = Annotated[Session, Depends(get_db)]


def get_detail_repo(db: DbDep) -> DetailRepositoryInterface:
    return DetailRepository(db)


def get_user_repo(db: DbDep) -> UserRepositoryInterface:
    return UserRepository(db)


UserRepositoryDep = Annotated[UserRepository, Depends(get_user_repo)]
DetailRepositoryDep = Annotated[DetailRepository, Depends(get_detail_repo)]


def get_detail_service(
        detail_repository: DetailRepositoryDep,
        user_repository: UserRepositoryDep
) -> DetailServiceInterface:
    return DetailService(detail_repository, user_repository)


def get_user_service(
        user_repository: UserRepositoryDep,
        detail_repository: DetailRepositoryDep
) -> UserServiceInterface:
    return UserService(user_repository, detail_repository)


def get_search_service() -> SearchServiceInterface:
    return SearchService(LegoParser())


def get_auth_service(user_repository: UserRepositoryDep) -> AuthServiceInterface:
    return AuthService(user_repository)


DetailServiceDep = Annotated[DetailService, Depends(get_detail_service)]
UserServiceDep = Annotated[UserService, Depends(get_user_service)]
SearchServiceDep = Annotated[SearchService, Depends(get_search_service)]
AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]
CredentialsDep = Annotated[HTTPBasicCredentials, Depends(HTTPBasic())]


def get_admin_service(user_service: UserServiceDep):
    return AdminService(user_service)


AdminServiceDep = Annotated[AdminService, Depends(get_admin_service)]


def get_current_user(
        credentials: Annotated[HTTPBasicCredentials, Depends(HTTPBasic(auto_error=False))],
        user_repository=Depends(get_user_repo)
) -> User:
    if credentials is None:
        raise UnauthedHttp
    user = user_repository.get_by_username(credentials.username)
    if not user or not compare_passwords(credentials.password, get_bytes_from_db_hex_hash(user.hashed_password)):
        raise UnauthedHttp
    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]
