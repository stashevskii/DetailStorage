from src.app.dtos.detail.requests.post import AddDetailDtoRequest
from src.app.dtos.detail.requests.put import FullUpdateDetailDtoRequest
from .interface import DetailInterface
from src.app.repositories.base import Repository
from ...db.db import Base
from ...models.detail import Detail


class DetailRepository(Repository, DetailInterface):
    table = Detail

    def get_all(self) -> list[Base]:
        response = self.session.query(self.table).all()
        return response

    def get(self, filter_params: dict, all_obj: bool) -> list[Base]:
        if all_obj:
            response = self.session.query(self.table).filter_by(**filter_params).all()
            return response
        else:
            response = self.session.query(self.table).filter_by(**filter_params).first()
            return [response]

    def add(self, ads: AddDetailDtoRequest) -> int:
        new_detail = self.table(**ads.model_dump())
        self.session.add(new_detail)
        self.session.commit()
        return new_detail.id

    def delete(self, id: int) -> None:
        detail_to_delete = self.session.query(self.table).filter_by(id=id).first()
        self.session.delete(detail_to_delete)
        self.session.commit()

    def full_update(self, id: int, uds: FullUpdateDetailDtoRequest) -> None:
        detail_to_update = self.session.query(self.table).filter_by(id=id).first()
        detail_to_update.lego_id = uds.new_lego_id
        detail_to_update.name = uds.new_name
        detail_to_update.quantity = uds.new_quantity
        detail_to_update.description = uds.new_description
        self.session.commit()

    def part_update(self, id: int, update_params: dict) -> None:
        detail_to_update = self.session.query(self.table).filter_by(id=id).first()
        for k, v in update_params.items():
            setattr(detail_to_update, k, v)
        self.session.commit()
