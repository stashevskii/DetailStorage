from fastapi import APIRouter, Depends
from src.app.api.errors import NotFoundUserHttp
from src.app.infrastructure.config import config
from src.app.domain.exceptions import (
    NotFoundDetailException,
    DetailAlreadyExistsException,
    NotFoundUserException
)
from src.app.domain.schemas import DetailFilter, DetailSchema, DetailCreate, DetailPartUpdate, DetailFullUpdate
from src.app.api.errors import NotFoundDetailHttp, DetailAlreadyExistsHttp
from src.app.domain.schemas import SuccessSchema
from src.app.core.utils import map_exceptions
from src.app.infrastructure.dependencies import DetailServiceDep, CurrentUserDep

router = APIRouter(prefix=config.detail_router_config.prefix, tags=config.detail_router_config.tags)


@router.get(
    "/",
    summary=config.detail_router_config.docs[1]["summary"],
    description=config.detail_router_config.docs[1]["description"],
)
@map_exceptions({NotFoundDetailException: NotFoundDetailHttp})
def get_detail(
        service: DetailServiceDep,
        current_user: CurrentUserDep,
        schema: DetailFilter = Depends()
) -> list[DetailSchema]:
    return service.get(current_user.id, schema)


@router.post(
    "/",
    summary=config.detail_router_config.docs[2]["summary"],
    description=config.detail_router_config.docs[2]["description"]
)
@map_exceptions({
    DetailAlreadyExistsException: DetailAlreadyExistsHttp,
    NotFoundUserException: NotFoundUserHttp
})
def add_detail(
        service: DetailServiceDep,
        current_user: CurrentUserDep,
        schema: DetailCreate = Depends()
) -> DetailSchema:
    return service.add(current_user.id, schema)


@router.delete(
    "/{id}",
    summary=config.detail_router_config.docs[3]["summary"],
    description=config.detail_router_config.docs[3]["description"]
)
@map_exceptions({NotFoundDetailException: NotFoundDetailHttp})
def delete_detail(id: int, service: DetailServiceDep, current_user: CurrentUserDep) -> SuccessSchema:
    return service.delete(id, current_user.id)


@router.put(
    "/{id}",
    summary=config.detail_router_config.docs[4]["summary"],
    description=config.detail_router_config.docs[4]["description"]
)
@map_exceptions({NotFoundDetailException: NotFoundDetailHttp})
def replace_detail(
        id: int,
        current_user: CurrentUserDep,
        service: DetailServiceDep,
        schema: DetailFullUpdate = Depends()
) -> DetailSchema:
    return service.replace(id, current_user.id, schema)


@router.patch(
    "/{id}",
    summary=config.detail_router_config.docs[5]["summary"],
    description=config.detail_router_config.docs[5]["description"]
)
@map_exceptions({NotFoundDetailException: NotFoundDetailHttp})
def part_update_detail(
        id: int,
        current_user: CurrentUserDep,
        service: DetailServiceDep,
        schema: DetailPartUpdate = Depends()
) -> DetailSchema:
    return service.part_update(id, current_user.id, schema)
