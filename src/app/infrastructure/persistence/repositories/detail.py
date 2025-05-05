from src.app.core.utils.dicts import ignore_dict_element, delete_nones_from_dict
from src.app.domain.schemas.detail import DetailCreate, DetailFilter, DetailPartUpdate
from src.app.domain.schemas.detail import DetailFullUpdate
from src.app.domain.interfaces.detail import DetailRepositoryInterface
from src.app.core.base.repository import Repository
from src.app.infrastructure.persistence.db import Base
from src.app.infrastructure.persistence.models.detail import Detail


class DetailRepository(Repository, DetailRepositoryInterface):
    table = Detail

    def get_all(self) -> list[Base]:
        return self.session.query(self.table).all()

    def get(self, schema: DetailFilter) -> list[Base]:
        query = self.session.query(self.table).filter_by(
            **ignore_dict_element(delete_nones_from_dict(schema.model_dump()), "all_obj")
        )
        return query.all() if schema.all_obj else [query.first()]

    def add(self, schema: DetailCreate) -> int:
        new_detail = self.table(**schema.model_dump())
        self.session.add(new_detail)
        self.session.commit()
        return new_detail.id

    def delete(self, id: int) -> None:
        detail_to_delete = self.session.query(self.table).filter_by(id=id).first()
        self.session.delete(detail_to_delete)
        self.session.commit()

    def full_update(self, id: int, schema: DetailFullUpdate) -> None:
        detail_to_update = self.session.query(self.table).filter_by(id=id).first()
        for k, v in schema.model_dump().items(): setattr(detail_to_update, k, v)
        self.session.commit()

    def part_update(self, id: int, schema: DetailPartUpdate) -> None:
        detail_to_update = self.session.query(self.table).filter_by(id=id).first()
        for k, v in delete_nones_from_dict(schema.model_dump()).items(): setattr(detail_to_update, k, v)
        self.session.commit()
