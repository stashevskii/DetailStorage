from fastapi import APIRouter, Depends

from src.app.api.errors import NotFoundUserHttpException
from src.app.infrastructure.config.main import config
from src.app.domain.exceptions.detail import (
    NotFoundDetailBasicException,
    DetailAlreadyExistsBasicException,
)
from src.app.domain.exceptions.user import NotFoundUserBasicException
from src.app.domain.schemas import DetailFilter, DetailSchema, DetailCreate, DetailPartUpdate, DetailFullUpdate
from src.app.api.errors import NotFoundDetailHttpException, DetailAlreadyExistsHttpException
from src.app.domain.schemas import SuccessSchema
from src.app.core.utils import map_exceptions
from src.app.infrastructure.dependencies import DetailServiceDep

router = APIRouter(prefix=config.detail_router_config.prefix, tags=config.detail_router_config.tags)


@router.get(
    "/",
    summary=config.detail_router_config.docs[1]["summary"],
    description=config.detail_router_config.docs[1]["description"],
)
@map_exceptions({NotFoundDetailBasicException: NotFoundDetailHttpException})
def get_detail(
        service: DetailServiceDep,
        schema: DetailFilter = Depends()
) -> list[DetailSchema]:
    return service.get(schema)


@router.post(
    "/",
    summary=config.detail_router_config.docs[2]["summary"],
    description=config.detail_router_config.docs[2]["description"]
)
@map_exceptions({
    DetailAlreadyExistsBasicException: DetailAlreadyExistsHttpException,
    NotFoundUserBasicException: NotFoundUserHttpException
})
def add_detail(
        service: DetailServiceDep,
        schema: DetailCreate = Depends()
) -> DetailSchema:
    return service.add(schema)


@router.delete(
    "/{id}",
    summary=config.detail_router_config.docs[3]["summary"],
    description=config.detail_router_config.docs[3]["description"]
)
@map_exceptions({NotFoundDetailBasicException: NotFoundDetailHttpException})
def delete_detail(id: int, service: DetailServiceDep) -> SuccessSchema:
    return service.delete(id)


@router.put(
    "/{id}",
    summary=config.detail_router_config.docs[4]["summary"],
    description=config.detail_router_config.docs[4]["description"]
)
@map_exceptions({NotFoundDetailBasicException: NotFoundDetailHttpException})
def replace_detail(
        id: int, service: DetailServiceDep,
        schema: DetailFullUpdate = Depends()
) -> DetailSchema:
    return service.replace(id, schema)


@router.patch("/{id}",
              summary=config.detail_router_config.docs[5]["summary"],
              description=config.detail_router_config.docs[5]["description"])
@map_exceptions({NotFoundDetailBasicException: NotFoundDetailHttpException})
def part_update_detail(
        id: int, service: DetailServiceDep,
        schema: DetailPartUpdate = Depends()
) -> DetailSchema:
    return service.part_update(id, schema)
