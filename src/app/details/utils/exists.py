from src.app.details.exceptions.business.business import (
    NotFoundDetailBasicException,
    DetailAlreadyExistsBasicException,
    NotFoundUserBasicException
)
from src.app.details.integrations.user_service_integration import check_user_exists
from src.app.details.repository.repository import DetailRepository


def check_detail_exist(repo: DetailRepository, id: int) -> bool:
    if id is None:
        return False

    all_details = repo.get_all()
    for i in all_details:
        if i.id == id:
            return True
    return False


def raise_exceptions_detail_not_found(repo: DetailRepository, id: int):
    if not check_detail_exist(repo, id):
        raise NotFoundDetailBasicException


def raise_exceptions_adding_detail(repo: DetailRepository, detail_id: int, user_id: int):
    if check_detail_exist(repo, detail_id):
        raise DetailAlreadyExistsBasicException
    if not check_user_exists(user_id):
        raise NotFoundUserBasicException
