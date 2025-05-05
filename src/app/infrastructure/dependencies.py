from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from src.app.domain.interfaces.detail import DetailRepositoryInterface
from src.app.domain.interfaces.user import UserRepositoryInterface
from src.app.domain.services.detail import DetailService
from src.app.domain.services.search import SearchService
from src.app.domain.services.user import UserService
from src.app.infrastructure.external.lego_parser import LegoParser
from src.app.infrastructure.persistence.db import get_db
from src.app.infrastructure.persistence.repositories.detail import DetailRepository
from src.app.infrastructure.persistence.repositories.user import UserRepository

DbDep = Annotated[Session, Depends(get_db)]


def get_detail_repo(db: DbDep):
    return DetailRepository(db)


def get_user_repo(db: DbDep):
    return UserRepository(db)


def get_detail_service(
        detail_repo: DetailRepositoryInterface = Depends(get_detail_repo),
        user_repo: UserRepositoryInterface = Depends(get_user_repo)
):
    return DetailService(detail_repo, user_repo)


def get_user_service(
        user_repo: UserRepositoryInterface = Depends(get_user_repo)
):
    return UserService(user_repo)

def get_search_service():
    return SearchService(LegoParser())

DetailServiceDep = Annotated[DetailService, Depends(get_detail_service)]
UserServiceDep = Annotated[UserService, Depends(get_user_service)]
SearchServiceDep = Annotated[SearchService, Depends(get_search_service)]
