from typing import Optional
from src.app.dependencies import DbDep
from src.app.entities.details.requests.get import GetDetailSchemaRequest
from src.app.entities.details.requests.patch import PartUpdateDetailSchemaRequest
from src.app.entities.details.requests.post import AddDetailSchemaRequest
from src.app.entities.details.requests.put import FullUpdateDetailSchemaRequest
from src.app.models.detail import Detail
from src.app.repositories.detail.repository import DetailRepository
from fastapi import HTTPException
from src.app.db.db import Base
from src.app.services.detail.utils import check_detail_exist


class DetailService:
    def __init__(self, session: DbDep):
        self.detail_repository = DetailRepository(session, Detail)

    def get_detail(self, gds: GetDetailSchemaRequest) -> list[Base]:
        get_params = {}
        for k, v in gds.model_dump().items():
            if v is not None:
                get_params[k] = v

        del get_params["all_obj"]
        response = self.detail_repository.get(get_params, gds.all_obj)
        if response == [None] or not response:
            raise HTTPException(status_code=422)

        res_response = []

        for i in response:
            res_response.append({
                "id": i.id,
                "lego_id": i.lego_id,
                "name": i.name,
                "quantity": i.quantity,
                "description": i.description
            })
        return res_response

    def add_detail(self, ads: AddDetailSchemaRequest) -> dict[int: Optional[int], str: bool] | HTTPException:
        if check_detail_exist(self.detail_repository, ads.id):
            raise HTTPException(status_code=422)
        new_id = self.detail_repository.add(ads)
        return {"id": new_id, "success": True}

    def delete_detail(self, id: int) -> dict[str: bool] | HTTPException:
        if not check_detail_exist(self.detail_repository, id):
            raise HTTPException(status_code=422)
        self.detail_repository.delete(id)
        return {"success": True}

    def full_update_detail(self, id, uds: FullUpdateDetailSchemaRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        if not check_detail_exist(self.detail_repository, id):
            raise HTTPException(status_code=422)
        self.detail_repository.full_update(id, uds)
        return {"success": True, "id": id}

    def part_update_detail(self, id, uds: PartUpdateDetailSchemaRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        if not check_detail_exist(self.detail_repository, id):
            raise HTTPException(status_code=422)
        update_params = {k: v for k, v in uds.model_dump().items() if v is not None}
        self.detail_repository.part_update(id, update_params)
        return {"success": True, "id": id}
