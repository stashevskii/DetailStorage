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


class DetailService(Service, DetailServiceInterface):
    def __init__(
            self,
            detail_repository: DetailRepositoryInterface,
            user_repository: UserRepositoryInterface
    ):
        super().__init__(detail_repository)
        self.user_repo = user_repository

    def get(self, schema: DetailFilter) -> dict:
        response = self.repository.get(schema)

        if response == [None] or not response: raise NotFoundDetailBasicException

        details_and_owners = []
        for i in response:
            details_and_owners.append(
                {
                    "detail": i.as_dict(),
                    "owner": i.user.as_dict()
                }
            )

        return {"data": details_and_owners}

    def add(self, schema: DetailCreate) -> dict[int: Optional[int], str: bool] | HTTPException:
        check_detail_raise_exceptions(self.repository, schema.id, check_exists=True)
        check_user_and_raise_exceptions(self.user_repo, schema.user_id, check_not_found=True)
        new_id = self.repository.add(schema)
        return {"id": new_id, "success": True}

    def delete(self, id: int) -> dict[str: bool] | HTTPException:
        check_detail_raise_exceptions(self.repository, id, check_not_found=True)
        self.repository.delete(id)
        return {"success": True}

    def full_update(self, id, schema: DetailFullUpdate) -> dict[int: Optional[int], str: bool] | HTTPException:
        check_detail_raise_exceptions(self.repository, id, check_not_found=True)
        self.repository.full_update(id, schema)
        return {"success": True, "id": id}

    def part_update(self, id, schema: DetailPartUpdate) -> dict[int: Optional[int], str: bool] | HTTPException:
        check_detail_raise_exceptions(self.repository, id, check_not_found=True)
        self.repository.part_update(id, schema)
        return {"success": True, "id": id}
