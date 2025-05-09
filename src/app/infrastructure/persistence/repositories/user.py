from typing import Type
from src.app.core.utils.dicts import ignore_dict_element, delete_nones_from_dict
from src.app.domain.schemas import UserFullUpdate, UserCreate, UserFilter, UserPartUpdate
from src.app.domain.abstractions.user import UserRepositoryInterface
from src.app.core.base.repository import Repository
from src.app.infrastructure.persistence.models.user import User
from src.app.core.utils.password import hash_password


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

    def replace(self, id: int, schema: UserFullUpdate) -> User | None:
        user_to_update = self.session.query(self.table).filter_by(id=id).first()
        for k, v in schema.model_dump().items():
            if k == "password":
                setattr(user_to_update, "hashed_password", hash_password(schema.password))
                continue
            setattr(user_to_update, k, v)
        self.session.commit()
        return user_to_update

    def part_update(self, id: int, schema: UserPartUpdate) -> User | None:
        user_to_update = self.session.query(self.table).filter_by(id=id).first()
        for k, v in delete_nones_from_dict(schema.model_dump()).items():
            setattr(user_to_update, k, v)
            if k == "password":
                setattr(user_to_update, "hashed_password", hash_password(schema.password))
                continue
        self.session.commit()
        return user_to_update
