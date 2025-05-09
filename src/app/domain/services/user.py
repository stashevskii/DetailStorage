from src.app.domain.schemas.user import UserFilter
from src.app.domain.schemas.user import UserPartUpdate
from src.app.domain.schemas.user import UserCreate
from src.app.domain.schemas.user import UserFullUpdate
from src.app.core.utils.exists import check_user_and_raise_exceptions
from src.app.core.base.service import Service
from src.app.domain.exceptions.user import NotFoundUserBasicException
from src.app.domain.interfaces.detail import DetailServiceInterface
from src.app.domain.interfaces.user import UserServiceInterface, UserRepositoryInterface
from src.app.infrastructure.persistence.models.user import User
from src.app.infrastructure.web.logger import get_logger

log = get_logger(__name__)


class UserService(Service, UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface, detail_service: DetailServiceInterface):
        super().__init__(user_repository)
        self.detail_service = detail_service

    def get_by_id(self, id: int) -> User:
        return self.repository.get_by_id(id=id)

    def get(self, schema: UserFilter) -> User:
        log.info("Getting user with following params: %s", schema)
        response = self.repository.get(schema)
        if response is None: raise NotFoundUserBasicException
        return response

    def add(self, schema: UserCreate) -> User:
        log.info("Adding user with following params: %s", schema)
        check_user_and_raise_exceptions(self.repository, schema.id, schema.email, schema.username, check_exists=True)
        return self.repository.add(schema)

    def delete(self, id: int) -> dict[str, bool]:
        log.info("Deleting user with id: %d", id)
        check_user_and_raise_exceptions(self.repository, id, check_not_found=True)
        log.info("Deleting user's (with %d) details", id)
        for i in self.get_by_id(id).details:
            self.detail_service.delete(i.id)
        self.repository.delete(id)
        return {"success": True}

    def replace(self, id, schema: UserFullUpdate) -> User:
        log.info("Replacing user with id %d and following params: %s", id, schema)
        check_user_and_raise_exceptions(self.repository, id, check_not_found=True)
        check_user_and_raise_exceptions(
            self.repository,
            email=schema.email,
            username=schema.username,
            check_exists=True
        )
        return self.repository.replace(id, schema)

    def part_update(self, id, schema: UserPartUpdate) -> User:
        log.info("Doing part update user with id %d and following params: %s", id, schema)
        check_user_and_raise_exceptions(self.repository, id, check_not_found=True)
        check_user_and_raise_exceptions(
            self.repository,
            email=schema.email,
            username=schema.username,
            check_exists=True
        )
        return self.repository.part_update(id, schema)
