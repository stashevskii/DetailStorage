from typing import Type
from src.app.core.utils import ignore_dict_element, delete_nones_from_dict
from src.app.domain.schemas import DetailPartUpdate, DetailFullUpdate
from src.app.domain.abstractions import DetailRepositoryInterface
from src.app.core.base import Repository
from src.app.infrastructure.persistence.models import Detail


class DetailRepository(Repository[Detail], DetailRepositoryInterface):
    table = Detail

    def get_all(self) -> list[Type[Detail]]:
        return self.session.query(self.table).all()

    def get(self, **kwargs) -> list[Detail] | list[Detail | None]:
        query = self.session.query(self.table).filter_by(
            **ignore_dict_element(delete_nones_from_dict(kwargs), "all_obj")
        )
        return query.all() if kwargs["all_obj"] else [query.first()]

    def add(self, **kwargs) -> Detail:
        new_detail = self.table(**kwargs)
        self.session.add(new_detail)
        self.session.commit()
        return new_detail

    def delete(self, id: int, user_id: int) -> None:
        detail_to_delete = self.session.query(self.table).filter_by(id=id, user_id=user_id).first()
        self.session.delete(detail_to_delete)
        self.session.commit()

    def __basic_update(
            self,
            id: int,
            user_id: int,
            schema: DetailFullUpdate | DetailPartUpdate,
            dict_func=lambda _: _
    ) -> Detail | None:
        detail_to_update = self.session.query(self.table).filter_by(id=id, user_id=user_id).first()
        for k, v in dict_func(schema.model_dump()).items():
            setattr(detail_to_update, k, v)
        self.session.commit()
        return detail_to_update

    def replace(self, id: int, user_id: int, schema: DetailFullUpdate) -> Detail | None:
        return self.__basic_update(id, user_id, schema)

    def part_update(self, id: int, user_id: int, schema: DetailPartUpdate) -> Detail | None:
        return self.__basic_update(id, user_id, schema, delete_nones_from_dict)
