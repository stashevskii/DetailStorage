from src.app.domain.schemas.user import UserFullUpdate
from src.app.domain.interfaces.user import UserRepositoryInterface
from src.app.core.common.repository import Repository
from src.app.db.db import Base
from src.app.domain.models.user import User
from src.app.utils.password import hash_password


class UserRepository(Repository, UserRepositoryInterface):
    table = User

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

    def add(self, add_params: dict) -> int:
        new_user = self.table(**add_params)
        self.session.add(new_user)
        self.session.commit()
        return new_user.id

    def delete(self, id: int) -> None:
        user_to_delete = self.session.query(self.table).filter_by(id=id).first()
        self.session.delete(user_to_delete)
        self.session.commit()

    def full_update(self, id: int, schema: UserFullUpdate) -> None:
        user_to_update = self.session.query(self.table).filter_by(id=id).first()
        user_to_update.username = schema.username
        user_to_update.email = schema.new_name
        user_to_update.hashed_password = hash_password(schema.password)
        self.session.commit()

    def part_update(self, id: int, update_params: dict) -> None:
        user_to_update = self.session.query(self.table).filter_by(id=id).first()
        for k, v in update_params.items():
            setattr(user_to_update, k, v)
        self.session.commit()
