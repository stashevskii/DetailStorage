from fastapi import Depends
from src.app.details.schemas.requests.get import GetDetailSchemaRequest
from src.app.details.schemas.requests.patch import PartUpdateDetailSchemaRequest
from src.app.details.schemas.requests.post import AddDetailSchemaRequest
from src.app.details.schemas.requests.put import FullUpdateDetailSchemaRequest
from src.app.details.schemas.responses.delete import DeleteDetailSchemaResponse
from src.app.details.schemas.responses.get import GetDetailSchemaResponse
from src.app.details.schemas.responses.patch import PartUpdateDetailSchemaResponse
from src.app.details.schemas.responses.post import AddDetailSchemaResponse
from src.app.details.schemas.responses.put import FullUpdateDetailSchemaResponse
from src.app.details.service.service import DetailService


def get_detail(service: DetailService = Depends(DetailService),
               gds: GetDetailSchemaRequest = Depends()) -> list[GetDetailSchemaResponse]:
    return service.get_detail(gds)


def add_detail(service: DetailService = Depends(DetailService),
               ads: AddDetailSchemaRequest = Depends()) -> AddDetailSchemaResponse:
    return service.add_detail(ads)


def delete_detail(id: int, service: DetailService = Depends(DetailService)) -> DeleteDetailSchemaResponse:
    return service.delete_detail(id)


def full_update_detail(id: int, service: DetailService = Depends(DetailService),
                       uds: FullUpdateDetailSchemaRequest = Depends()) -> FullUpdateDetailSchemaResponse:
    return service.full_update_detail(id, uds)


def part_update_detail(id: int, service: DetailService = Depends(DetailService),
                       uds: PartUpdateDetailSchemaRequest = Depends()) -> PartUpdateDetailSchemaResponse:
    return service.part_update_detail(id, uds)
