from src.app.domain.schemas import DetailFilter, DetailPartUpdate, DetailCreate, DetailFullUpdate
from src.app.core.utils.exists import check_detail_raise_exceptions, check_user_and_raise_exceptions
from src.app.core.base.service import Service
from src.app.domain.exceptions.detail import NotFoundDetailBasicException
from src.app.domain.interfaces.detail import DetailServiceInterface, DetailRepositoryInterface
from src.app.domain.interfaces.user import UserRepositoryInterface
from src.app.infrastructure.persistence.models.detail import Detail
from src.app.infrastructure.web.logger import get_logger

log = get_logger(__name__)


class DetailService(Service, DetailServiceInterface):
    def __init__(
            self,
            detail_repository: DetailRepositoryInterface,
            user_repository: UserRepositoryInterface
    ):
        super().__init__(detail_repository)
        self.user_repo = user_repository

    def get(self, schema: DetailFilter) -> list[Detail]:
        log.info("Getting details with following param: %s", schema)
        response = self.repository.get(schema)
        if response == [None] or not response: raise NotFoundDetailBasicException
        return [i for i in response]

    def add(self, schema: DetailCreate) -> Detail:
        log.info("Adding detail with following params: %s", schema)
        check_detail_raise_exceptions(self.repository, schema.id, check_exists=True)
        check_user_and_raise_exceptions(self.user_repo, schema.user_id, check_not_found=True)
        return self.repository.add(schema)

    def delete(self, id: int) -> dict[str: bool]:
        log.info("Deleting detail with id: %d", id)
        check_detail_raise_exceptions(self.repository, id, check_not_found=True)
        self.repository.delete(id)
        return {"success": True}

    def replace(self, id, schema: DetailFullUpdate) -> Detail:
        log.info("Replacing detail with id %d and following params: %s", id, schema)
        check_detail_raise_exceptions(self.repository, id, check_not_found=True)
        return self.repository.replace(id, schema)

    def part_update(self, id, schema: DetailPartUpdate) -> Detail:
        log.info("Doing part update detail with id %d and following params: %s", id, schema)
        check_detail_raise_exceptions(self.repository, id, check_not_found=True)
        return self.repository.part_update(id, schema)
