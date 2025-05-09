from typing import Type
from src.app.core.utils.dicts import ignore_dict_element, delete_nones_from_dict
from src.app.domain.schemas import DetailCreate, DetailFilter, DetailPartUpdate, DetailFullUpdate
from src.app.domain.abstractions.detail import DetailRepositoryInterface
from src.app.core.base.repository import Repository
from src.app.infrastructure.persistence.models.detail import Detail


class DetailRepository(Repository, DetailRepositoryInterface):
    table = Detail

    def get_all(self) -> list[Type[Detail]]:
        return self.session.query(self.table).all()

    def get(self, schema: DetailFilter) -> list[Type[Detail]] | list[Type[Detail] | None]:
        query = self.session.query(self.table).filter_by(
            **ignore_dict_element(delete_nones_from_dict(schema.model_dump()), "all_obj")
        )
        return query.all() if schema.all_obj else [query.first()]

    def add(self, schema: DetailCreate) -> Detail:
        new_detail = self.table(**schema.model_dump())
        self.session.add(new_detail)
        self.session.commit()
        return new_detail

    def delete(self, id: int) -> None:
        detail_to_delete = self.session.query(self.table).filter_by(id=id).first()
        self.session.delete(detail_to_delete)
        self.session.commit()

    def basic_update(self, id: int, schema: DetailFullUpdate | DetailPartUpdate, dict_func=lambda _: _):
        detail_to_update = self.session.query(self.table).filter_by(id=id).first()
        for k, v in dict_func(schema.model_dump().items()): setattr(detail_to_update, k, v)
        self.session.commit()
        return detail_to_update

    def replace(self, id: int, schema: DetailFullUpdate) -> None:
        return self.basic_update(id, schema)

    def part_update(self, id: int, schema: DetailPartUpdate) -> None:
        return self.basic_update(id, schema, delete_nones_from_dict)
