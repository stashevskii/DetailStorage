from src.app.core.utils.exists import check_user_owns_detail_and_raise_exceptions
from src.app.domain.schemas import DetailFilter, DetailPartUpdate, DetailCreate, DetailFullUpdate
from src.app.core.utils import check_detail_raise_exceptions, check_user_and_raise_exceptions, get_logger
from src.app.core.base import Service
from src.app.domain.exceptions import NotFoundDetailException
from src.app.domain.abstractions import DetailServiceInterface, DetailRepositoryInterface, UserRepositoryInterface
from src.app.infrastructure.persistence.models import Detail

log = get_logger(__name__)


class DetailService(Service, DetailServiceInterface):
    def __init__(
            self,
            detail_repository: DetailRepositoryInterface,
            user_repository: UserRepositoryInterface
    ):
        super().__init__(detail_repository)
        self.user_repo = user_repository

    def get(self, user_id: int, schema: DetailFilter) -> list[Detail]:
        log.info("Getting details with following params: %s", schema)
        response = self.repository.get(**schema.model_dump(), user_id=user_id)
        if response == [None] or not response: raise NotFoundDetailException
        return [i for i in response]

    def add(self, user_id: int, schema: DetailCreate) -> Detail:
        log.info("Adding detail with following params: %s", schema)
        check_detail_raise_exceptions(self.repository, schema.id, check_exists=True)
        check_user_and_raise_exceptions(self.user_repo, user_id, check_not_found=True)
        return self.repository.add(**schema.model_dump(), user_id=user_id)

    def delete(self, detail_id: int, user_id: int) -> dict[str, bool]:
        log.info("Deleting detail with id: %d", detail_id)
        check_detail_raise_exceptions(self.repository, detail_id, check_not_found=True)
        check_user_owns_detail_and_raise_exceptions(self.user_repo, detail_id, user_id)
        self.repository.delete(detail_id, user_id)
        return {"success": True}

    def replace(self, detail_id: int, user_id: int, schema: DetailFullUpdate) -> Detail:
        log.info("Replacing detail with id %d and following params: %s", id, schema)
        check_detail_raise_exceptions(self.repository, detail_id, check_not_found=True)
        check_user_owns_detail_and_raise_exceptions(self.user_repo, detail_id, user_id)
        return self.repository.replace(detail_id, user_id, schema)

    def part_update(self, detail_id: int, user_id: int, schema: DetailPartUpdate) -> Detail:
        log.info("Doing part update detail with id %d and following params: %s", detail_id, schema)
        check_detail_raise_exceptions(self.repository, detail_id, check_not_found=True)
        check_user_owns_detail_and_raise_exceptions(self.user_repo, detail_id, user_id)
        return self.repository.part_update(detail_id, user_id, schema)
