from fastapi import APIRouter
from src.app.api.errors import InvalidCredentialsHttp
from src.app.domain.exceptions.auth import InvalidCredentialsException
from src.app.domain.schemas.schemas import LoginResponse
from src.app.infrastructure.config import config
from src.app.infrastructure.dependencies import AuthServiceDep, CredentialsDep
from src.app.core.utils import map_exceptions

router = APIRouter(prefix=config.auth_router_config.prefix, tags=config.auth_router_config.tags )


@router.post(
    "/login",
    summary=config.auth_router_config.docs[1]["summary"],
    description=config.auth_router_config.docs[1]["description"]
)
@map_exceptions({InvalidCredentialsException: InvalidCredentialsHttp})
def login(credentials: CredentialsDep, service: AuthServiceDep) -> LoginResponse:
    return service.login(credentials)
