from typing import Optional
from fastapi import HTTPException
from src.app.domain.schemas.detail import DetailFilter
from src.app.domain.schemas.detail import DetailPartUpdate
from src.app.domain.schemas.detail import DetailCreate
from src.app.domain.schemas.detail import DetailFullUpdate
from src.app.core.utils.exists import check_detail_raise_exceptions, check_user_and_raise_exceptions
from src.app.core.base.service import Service
from src.app.domain.exceptions.detail import (
    NotFoundDetailBasicException,
)
from ..interfaces.detail import DetailServiceInterface, DetailRepositoryInterface
from ..interfaces.user import UserRepositoryInterface
from ...infrastructure.persistence.models.detail import Detail


class DetailService(Service, DetailServiceInterface):
    def __init__(
            self,
            detail_repository: DetailRepositoryInterface,
            user_repository: UserRepositoryInterface
    ):
        super().__init__(detail_repository)
        self.user_repo = user_repository

    def get(self, schema: DetailFilter) -> list[Detail]:
        response = self.repository.get(schema)
        if response == [None] or not response: raise NotFoundDetailBasicException
        return [i for i in response]

    def add(self, schema: DetailCreate) -> dict[int: Optional[int], str: bool] | HTTPException:
        check_detail_raise_exceptions(self.repository, schema.id, check_exists=True)
        check_user_and_raise_exceptions(self.user_repo, schema.user_id, check_not_found=True)
        return self.repository.add(schema)

    def delete(self, id: int) -> dict[str: bool] | HTTPException:
        check_detail_raise_exceptions(self.repository, id, check_not_found=True)
        self.repository.delete(id)
        return {"success": True}

    def replace(self, id, schema: DetailFullUpdate) -> dict[int: Optional[int], str: bool] | HTTPException:
        check_detail_raise_exceptions(self.repository, id, check_not_found=True)
        return self.repository.replace(id, schema)

    def part_update(self, id, schema: DetailPartUpdate) -> dict[int: Optional[int], str: bool] | HTTPException:
        check_detail_raise_exceptions(self.repository, id, check_not_found=True)
        return self.repository.part_update(id, schema)
