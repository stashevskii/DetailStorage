from src.app.domain.schemas import UserFilter, UserPartUpdate, UserCreate, UserFullUpdate
from src.app.core.utils import check_user_and_raise_exceptions, get_logger
from src.app.core.base import Service
from src.app.domain.exceptions import NotFoundUserException
from src.app.domain.abstractions import UserServiceInterface, UserRepositoryInterface, DetailRepositoryInterface
from src.app.infrastructure.persistence.models import User

log = get_logger(__name__)


class UserService(Service, UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface, detail_repository: DetailRepositoryInterface):
        super().__init__(user_repository)
        self.detail_repository = detail_repository

    def get_all(self):
        log.info("Getting all users")
        return self.repository.get_all()

    def get(self, schema: UserFilter) -> User:
        log.info("Getting user with following params: %s", schema)
        response = self.repository.get(schema)
        if response is None: raise NotFoundUserException
        return response

    def add(self, schema: UserCreate) -> User:
        log.info("Adding user with following params: %s", schema)
        check_user_and_raise_exceptions(self.repository, schema.id, schema.email, schema.username, check_exists=True)
        return self.repository.add(schema)

    def delete(self, id: int) -> dict[str, bool]:
        log.info("Deleting user with id: %d", id)
        check_user_and_raise_exceptions(self.repository, id, check_not_found=True)
        log.info("Deleting user's (with id %d) details", id)
        # delete all user details
        for i in self.repository.get_by_id(id=id).details:
            self.detail_repository.delete(i.id, id)
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
