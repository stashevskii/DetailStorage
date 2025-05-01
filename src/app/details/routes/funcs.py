from fastapi import Depends
from src.app.details.exceptions.http.http import NotFoundDetailHttpException, DetailAlreadyExistsHttpException
from src.app.details.exceptions.business.business import NotFoundDetailBasicException, DetailAlreadyExistsBasicException
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
from src.app.details.utils.decorators import map_exceptions


@map_exceptions(NotFoundDetailBasicException, NotFoundDetailHttpException)
def get_detail(service: DetailService = Depends(DetailService),
               schema: GetDetailSchemaRequest = Depends()) -> list[GetDetailSchemaResponse]:
    return service.get(schema)


@map_exceptions(DetailAlreadyExistsBasicException, DetailAlreadyExistsHttpException)
def add_detail(service: DetailService = Depends(DetailService),
               schema: AddDetailSchemaRequest = Depends()) -> AddDetailSchemaResponse:
    return service.add(schema)


@map_exceptions(NotFoundDetailBasicException, NotFoundDetailHttpException)
def delete_detail(id: int, service: DetailService = Depends(DetailService)) -> DeleteDetailSchemaResponse:
    return service.delete(id)


@map_exceptions(NotFoundDetailBasicException, NotFoundDetailHttpException)
def full_update_detail(id: int, service: DetailService = Depends(DetailService),
                       schema: FullUpdateDetailSchemaRequest = Depends()) -> FullUpdateDetailSchemaResponse:
    return service.full_update(id, schema)


@map_exceptions(NotFoundDetailBasicException, NotFoundDetailHttpException)
def part_update_detail(id: int, service: DetailService = Depends(DetailService),
                       schema: PartUpdateDetailSchemaRequest = Depends()) -> PartUpdateDetailSchemaResponse:
    return service.part_update(id, schema)
