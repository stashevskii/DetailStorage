from fastapi import Depends
from src.app.dtos.detail.requests.get import GetDetailDtoRequest
from src.app.dtos.detail.requests.patch import PartUpdateDetailDtoRequest
from src.app.dtos.detail.requests.post import AddDetailDtoRequest
from src.app.dtos.detail.requests.put import FullUpdateDetailDtoRequest
from src.app.dtos.detail.responses.delete import DeleteDetailDtoResponse
from src.app.dtos.detail.responses.get import GetDetailDtoResponse
from src.app.dtos.detail.responses.patch import PartUpdateDetailDtoResponse
from src.app.dtos.detail.responses.post import AddDetailDtoResponse
from src.app.dtos.detail.responses.put import FullUpdateDetailDtoResponse
from src.app.services.detail.service import DetailService


def get_detail(service: DetailService = Depends(DetailService),
               gds: GetDetailDtoRequest = Depends()) -> list[GetDetailDtoResponse]:
    return service.get_detail(gds)


def add_detail(service: DetailService = Depends(DetailService),
               ads: AddDetailDtoRequest = Depends()) -> AddDetailDtoResponse:
    return service.add_detail(ads)


def delete_detail(id: int, service: DetailService = Depends(DetailService)) -> DeleteDetailDtoResponse:
    return service.delete_detail(id)


def full_update_detail(id: int, service: DetailService = Depends(DetailService),
                       uds: FullUpdateDetailDtoRequest = Depends()) -> FullUpdateDetailDtoResponse:
    return service.full_update_detail(id, uds)


def part_update_detail(id: int, service: DetailService = Depends(DetailService),
                       uds: PartUpdateDetailDtoRequest = Depends()) -> PartUpdateDetailDtoResponse:
    return service.part_update_detail(id, uds)
