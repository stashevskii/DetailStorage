from typing import Optional
from fastapi import HTTPException

from src.app.core.utils.dependencies import DbDep
from src.app.domain.schemas.detail import DetailFilter
from src.app.domain.schemas.detail import DetailPartUpdate
from src.app.domain.schemas.detail import DetailCreate
from src.app.domain.schemas.detail import DetailFullUpdate
from src.app.infrastructure.persistence.models.detail import Detail
from src.app.infrastructure.persistence.repositories.detail import DetailRepository
from src.app.core.utils.exists import (
    raise_exceptions_adding_detail,
    raise_exceptions_detail_not_found, raise_exceptions_user_not_exists
)
from src.app.core.base.service import Service
from src.app.domain.exceptions.detail import (
    NotFoundDetailBasicException,
)
from ..interfaces.detail import DetailServiceInterface
from src.app.infrastructure.persistence.repositories.user import UserRepository
from src.app.infrastructure.persistence.models.user import User


class DetailService(Service, DetailServiceInterface):
    def __init__(
            self,
            session: DbDep,
    ):
        super().__init__(DetailRepository(session, Detail))
        self.user_repo = UserRepository(session, User)

    def get(self, schema: DetailFilter) -> dict:
        get_params = {k: v for k, v in schema.model_dump().items() if v is not None}

        del get_params["all_obj"]
        response = self.repository.get(get_params, schema.all_obj)
        if response == [None] or not response:
            raise NotFoundDetailBasicException

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
        raise_exceptions_adding_detail(self.repository, schema.id)
        raise_exceptions_user_not_exists(self.user_repo, schema.user_id)
        new_id = self.repository.add(schema)
        return {"id": new_id, "success": True}

    def delete(self, id: int) -> dict[str: bool] | HTTPException:
        raise_exceptions_detail_not_found(self.repository, id)
        self.repository.delete(id)
        return {"success": True}

    def full_update(self, id, schema: DetailFullUpdate) -> dict[int: Optional[int],
                                                                        str: bool] | HTTPException:
        raise_exceptions_detail_not_found(self.repository, id)
        self.repository.full_update(id, schema)
        return {"success": True, "id": id}

    def part_update(self, id, schema: DetailPartUpdate) -> dict[int: Optional[int],
                                                                        str: bool] | HTTPException:
        raise_exceptions_detail_not_found(self.repository, id)
        update_params = {k: v for k, v in schema.model_dump().items() if v is not None}
        self.repository.part_update(id, update_params)
        return {"success": True, "id": id}
