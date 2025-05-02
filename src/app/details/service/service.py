from typing import Optional, Any
from fastapi import HTTPException
from src.app.details.utils.dependencies import DbDep
from src.app.details.schemas.requests.get import GetDetailSchemaRequest
from src.app.details.schemas.requests.patch import PartUpdateDetailSchemaRequest
from src.app.details.schemas.requests.post import AddDetailSchemaRequest
from src.app.details.schemas.requests.put import FullUpdateDetailSchemaRequest
from src.app.details.models.models import Detail
from src.app.details.repository.repository import DetailRepository
from src.app.details.utils.exists import (
    raise_exceptions_adding_detail,
    raise_exceptions_detail_not_found
)
from src.app.details.core.common.service import Service
from .interface import DetailServiceInterface
from src.app.details.exceptions.business.business import (
    NotFoundDetailBasicException,
)
from ..integrations.user_service_integration import get_user


class DetailService(Service, DetailServiceInterface):
    def __init__(self, session: DbDep):
        super().__init__(DetailRepository(session, Detail))

    def get(self, schema: GetDetailSchemaRequest) -> dict[str, list[dict[str, Any]]]:
        get_params = {}
        for k, v in schema.model_dump().items():
            if v is not None:
                get_params[k] = v

        del get_params["all_obj"]
        response = self.repository.get(get_params, schema.all_obj)
        if response == [None] or not response:
            raise NotFoundDetailBasicException

        res_response = []

        for i in response:
            res_response.append({"detail": i.as_dict(), "owner": get_user(i.user_id)})
        return {"data": res_response}

    def add(self, schema: AddDetailSchemaRequest) -> dict[int: Optional[int], str: bool] | HTTPException:
        raise_exceptions_adding_detail(self.repository, schema.id, schema.user_id)
        new_id = self.repository.add(schema)
        return {"id": new_id, "success": True}

    def delete(self, id: int) -> dict[str: bool] | HTTPException:
        raise_exceptions_detail_not_found(self.repository, id)
        self.repository.delete(id)
        return {"success": True}

    def full_update(self, id, schema: FullUpdateDetailSchemaRequest) -> dict[int: Optional[int],
                                                                        str: bool] | HTTPException:
        raise_exceptions_detail_not_found(self.repository, id)
        self.repository.full_update(id, schema)
        return {"success": True, "id": id}

    def part_update(self, id, schema: PartUpdateDetailSchemaRequest) -> dict[int: Optional[int],
                                                                        str: bool] | HTTPException:
        raise_exceptions_detail_not_found(self.repository, id)
        update_params = {k: v for k, v in schema.model_dump().items() if v is not None}
        self.repository.part_update(id, update_params)
        return {"success": True, "id": id}
