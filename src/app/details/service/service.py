from typing import Optional
from fastapi import HTTPException
from src.app.core.shared.dependencies import DbDep
from src.app.details.schemas.requests.get import GetDetailSchemaRequest
from src.app.details.schemas.requests.patch import PartUpdateDetailSchemaRequest
from src.app.details.schemas.requests.post import AddDetailSchemaRequest
from src.app.details.schemas.requests.put import FullUpdateDetailSchemaRequest
from src.app.details.models.models import Detail
from src.app.details.repository.repository import DetailRepository
from src.app.core.db import Base
from src.app.details.utils import check_detail_exist
from src.app.core.common.service import Service
from .interface import DetailServiceInterface
from ..exceptions import not_found_detail_exception


class DetailService(Service, DetailServiceInterface):
    def __init__(self, session: DbDep):
        super().__init__(DetailRepository(session, Detail))

    def get_detail(self, gds: GetDetailSchemaRequest) -> list[Base]:
        get_params = {}
        for k, v in gds.model_dump().items():
            if v is not None:
                get_params[k] = v

        del get_params["all_obj"]
        response = self.repository.get(get_params, gds.all_obj)
        if response == [None] or not response:
            raise not_found_detail_exception

        res_response = []

        for i in response:
            res_response.append(i.as_dict())
        return res_response

    def add_detail(self, ads: AddDetailSchemaRequest) -> dict[int: Optional[int], str: bool] | HTTPException:
        if check_detail_exist(self.repository, ads.id):
            raise not_found_detail_exception
        new_id = self.repository.add(ads)
        return {"id": new_id, "success": True}

    def delete_detail(self, id: int) -> dict[str: bool] | HTTPException:
        if not check_detail_exist(self.repository, id):
            raise not_found_detail_exception
        self.repository.delete(id)
        return {"success": True}

    def full_update_detail(self, id, uds: FullUpdateDetailSchemaRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        if not check_detail_exist(self.repository, id):
            raise not_found_detail_exception
        self.repository.full_update(id, uds)
        return {"success": True, "id": id}

    def part_update_detail(self, id, uds: PartUpdateDetailSchemaRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        if not check_detail_exist(self.repository, id):
            raise not_found_detail_exception
        update_params = {k: v for k, v in uds.model_dump().items() if v is not None}
        self.repository.part_update(id, update_params)
        return {"success": True, "id": id}
