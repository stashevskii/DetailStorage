from src.app.details.repository.repository import DetailRepository


def check_detail_exist(repo: DetailRepository, id: int) -> bool:
    if id is None:
        return False

    all_details = repo.get_all()
    for i in all_details:
        if i.id == id:
            return True
    return False
