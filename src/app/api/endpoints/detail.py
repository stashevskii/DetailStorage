from typing import Dict

from fastapi import APIRouter, Depends

from src.app.api.errors.http.user import NotFoundUserHttpException
from src.app.core.config import config
from src.app.domain.exceptions.detail import (
    NotFoundDetailBasicException,
    DetailAlreadyExistsBasicException,
)
from src.app.domain.exceptions.user import NotFoundUserBasicException
from src.app.domain.schemas.detail.requests.get import GetDetailSchemaRequest
from src.app.domain.schemas.detail.responses.get import GetDetailSchemaResponse
from src.app.domain.schemas.user.responses.get import GetUserSchemaResponse
from src.app.domain.services.detail import DetailService
from src.app.api.errors.http.detail import NotFoundDetailHttpException, DetailAlreadyExistsHttpException
from src.app.domain.schemas.detail.requests.patch import PartUpdateDetailSchemaRequest
from src.app.domain.schemas.detail.requests.post import AddDetailSchemaRequest
from src.app.domain.schemas.detail.requests.put import FullUpdateDetailSchemaRequest
from src.app.domain.schemas.detail.responses.delete import DeleteDetailSchemaResponse
from src.app.domain.schemas.detail.responses.patch import PartUpdateDetailSchemaResponse
from src.app.domain.schemas.detail.responses.post import AddDetailSchemaResponse
from src.app.domain.schemas.detail.responses.put import FullUpdateDetailSchemaResponse
from src.app.utils.decorators import map_exceptions

router = APIRouter(prefix=config.detail_router_config.prefix, tags=config.detail_router_config.tags)


@router.get(
    "/",
    summary=config.detail_router_config.docs[1]["summary"],
    description=config.detail_router_config.docs[1]["description"],
)
@map_exceptions((NotFoundDetailBasicException,), (NotFoundDetailHttpException,))
def get_detail(
        service: DetailService = Depends(DetailService),
        schema: GetDetailSchemaRequest = Depends()
) -> Dict[str, list[Dict[str, GetDetailSchemaResponse | Dict[str, list[GetUserSchemaResponse]]]]]:
    return service.get(schema)


@router.post(
    "/",
    summary=config.detail_router_config.docs[2]["summary"],
    description=config.detail_router_config.docs[2]["description"]
)
@map_exceptions((DetailAlreadyExistsBasicException, NotFoundUserBasicException),
                (DetailAlreadyExistsHttpException, NotFoundUserHttpException))
def add_detail(
        service: DetailService = Depends(DetailService),
        schema: AddDetailSchemaRequest = Depends()
) -> AddDetailSchemaResponse:
    return service.add(schema)


@router.delete(
    "/{id}",
    summary=config.detail_router_config.docs[3]["summary"],
    description=config.detail_router_config.docs[3]["description"]
)
@map_exceptions((NotFoundDetailBasicException,), (NotFoundDetailHttpException,))
def delete_detail(id: int, service: DetailService = Depends(DetailService)) -> DeleteDetailSchemaResponse:
    return service.delete(id)


@router.put(
    "/{id}",
    summary=config.detail_router_config.docs[4]["summary"],
    description=config.detail_router_config.docs[4]["description"]
)
@map_exceptions((NotFoundDetailBasicException,), (NotFoundDetailHttpException,))
def full_update_detail(
        id: int, service: DetailService = Depends(DetailService),
        schema: FullUpdateDetailSchemaRequest = Depends()
) -> FullUpdateDetailSchemaResponse:
    return service.full_update(id, schema)


@router.patch("/{id}",
              summary=config.detail_router_config.docs[5]["summary"],
              description=config.detail_router_config.docs[5]["description"])
@map_exceptions((NotFoundDetailBasicException,), (NotFoundDetailHttpException,))
def part_update_detail(
        id: int, service: DetailService = Depends(DetailService),
        schema: PartUpdateDetailSchemaRequest = Depends()
) -> PartUpdateDetailSchemaResponse:
    return service.part_update(id, schema)
