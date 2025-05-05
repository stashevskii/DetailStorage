from src.app.core.utils.dicts import ignore_dict_element, delete_nones_from_dict
from src.app.domain.schemas.user import UserFullUpdate, UserCreate, UserFilter, UserPartUpdate
from src.app.domain.interfaces.user import UserRepositoryInterface
from src.app.core.base.repository import Repository
from src.app.infrastructure.persistence.db import Base
from src.app.infrastructure.persistence.models.user import User
from src.app.core.utils.password import hash_password


class UserRepository(Repository, UserRepositoryInterface):
    table = User

    def get_all(self) -> list[Base]:
        return self.session.query(self.table).all()

    def get(self, schema: UserFilter) -> list[Base]:
        query = self.session.query(self.table).filter_by(
            **ignore_dict_element(delete_nones_from_dict(schema.model_dump()), "all_obj")
        )
        return query.all() if schema.all_obj else [query.first()]

    def add(self, schema: UserCreate) -> int:
        new_detail = self.table(
            **ignore_dict_element(schema.model_dump(), "password")
              | {"hashed_password": hash_password(schema.password)}
        )
        self.session.add(new_detail)
        self.session.commit()
        return new_detail.id

    def delete(self, id: int) -> None:
        detail_to_delete = self.session.query(self.table).filter_by(id=id).first()
        self.session.delete(detail_to_delete)
        self.session.commit()

    def full_update(self, id: int, schema: UserFullUpdate) -> None:
        detail_to_update = self.session.query(self.table).filter_by(id=id).first()
        for k, v in schema.model_dump().items():
            if k == "password":
                setattr(detail_to_update, "hashed_password", hash_password(schema.password))
                continue
            setattr(detail_to_update, k, v)
        self.session.commit()

    def part_update(self, id: int, schema: UserPartUpdate) -> None:
        detail_to_update = self.session.query(self.table).filter_by(id=id).first()
        for k, v in delete_nones_from_dict(schema.model_dump()).items():
            setattr(detail_to_update, k, v)
            if k == "password":
                setattr(detail_to_update, "hashed_password", hash_password(schema.password))
                continue
        self.session.commit()
