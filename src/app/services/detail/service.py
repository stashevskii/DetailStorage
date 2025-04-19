from typing import Optional
from src.app.dependencies import DbDep
from src.app.dtos.detail.requests.get import GetDetailDtoRequest
from src.app.dtos.detail.requests.patch import PartUpdateDetailDtoRequest
from src.app.dtos.detail.requests.post import AddDetailDtoRequest
from src.app.dtos.detail.requests.put import FullUpdateDetailDtoRequest
from src.app.models.detail import Detail
from src.app.repositories.detail.repository import DetailRepository
from fastapi import HTTPException
from src.app.db.db import Base
from src.app.services.detail.utils import check_detail_exist


class DetailService:
    def __init__(self, session: DbDep):
        self.detail_repository = DetailRepository(session, Detail)

    def get_detail(self, gds: GetDetailDtoRequest) -> list[Base]:
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
            res_response.append(i.as_dict())
        return res_response

    def add_detail(self, ads: AddDetailDtoRequest) -> dict[int: Optional[int], str: bool] | HTTPException:
        if check_detail_exist(self.detail_repository, ads.id):
            raise HTTPException(status_code=422)
        new_id = self.detail_repository.add(ads)
        return {"id": new_id, "success": True}

    def delete_detail(self, id: int) -> dict[str: bool] | HTTPException:
        if not check_detail_exist(self.detail_repository, id):
            raise HTTPException(status_code=422)
        self.detail_repository.delete(id)
        return {"success": True}

    def full_update_detail(self, id, uds: FullUpdateDetailDtoRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        if not check_detail_exist(self.detail_repository, id):
            raise HTTPException(status_code=422)
        self.detail_repository.full_update(id, uds)
        return {"success": True, "id": id}

    def part_update_detail(self, id, uds: PartUpdateDetailDtoRequest) -> dict[int: Optional[int],
                                                                            str: bool] | HTTPException:
        if not check_detail_exist(self.detail_repository, id):
            raise HTTPException(status_code=422)
        update_params = {k: v for k, v in uds.model_dump().items() if v is not None}
        self.detail_repository.part_update(id, update_params)
        return {"success": True, "id": id}
