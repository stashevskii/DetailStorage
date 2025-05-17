from src.app.core.utils import get_logger
from src.app.domain.abstractions import UserServiceInterface
from src.app.domain.schemas import UserCreate, UserFullUpdate, UserPartUpdate
from src.app.infrastructure.persistence.models import User

log = get_logger(__name__)


class AdminService:
    def __init__(self, user_service: UserServiceInterface):
        self.user_service = user_service

    def get_all(self) -> list[User]:
        return self.user_service.get_all()

    def add(self, schema: UserCreate) -> User:
        return self.user_service.add(schema)

    def delete(self, id: int) -> dict[str, bool]:
        return self.user_service.delete(id)

    def replace(self, id: int, schema: UserFullUpdate) -> User:
        return self.user_service.replace(id, schema)

    def part_update(self, id: int, schema: UserPartUpdate) -> User:
        return self.user_service.part_update(id, schema)
