from typing import Type
from src.app.core.utils import ignore_dict_element, delete_nones_from_dict, hash_password
from src.app.domain.schemas import UserFullUpdate, UserCreate, UserFilter, UserPartUpdate
from src.app.domain.abstractions.user import UserRepositoryInterface
from src.app.core.base import Repository
from src.app.infrastructure.persistence.models.user import User


class UserRepository(Repository, UserRepositoryInterface):
    table = User

    def get_all(self) -> list[Type[User]]:
        return self.session.query(self.table).all()

    def get(self, schema: UserFilter) -> User | None:
        return self.session.query(self.table).filter_by(**delete_nones_from_dict(schema.model_dump())).first()

    def get_by_id(self, id: int) -> User | None:
        return self.session.query(self.table).filter_by(id=id).first()

    def add(self, schema: UserCreate) -> User:
        new_user = self.table(
            **ignore_dict_element(schema.model_dump(), "password") | {"hashed_password": hash_password(schema.password)}
        )
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def delete(self, id: int) -> None:
        user_to_delete = self.session.query(self.table).filter_by(id=id).first()
        self.session.delete(user_to_delete)
        self.session.commit()

    def basic_update(self, id: int, schema: UserFullUpdate | UserPartUpdate, dict_func=lambda _: _):
        user_to_update = self.session.query(self.table).filter_by(id=id).first()
        for k, v in dict_func(schema.model_dump().items()):
            if k == "password":
                setattr(user_to_update, "hashed_password", hash_password(schema.password))
                continue
            setattr(user_to_update, k, v)
        self.session.commit()
        return user_to_update

    def replace(self, id: int, schema: UserFullUpdate) -> User | None:
        return self.basic_update(id, schema)

    def part_update(self, id: int, schema: UserPartUpdate) -> User | None:
        return self.basic_update(id, schema, delete_nones_from_dict)
