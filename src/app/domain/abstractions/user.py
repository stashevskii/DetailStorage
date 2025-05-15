from abc import ABC, abstractmethod
from .basic import CrudInterface, GetAllInterface


class UserRepositoryInterface(CrudInterface, GetAllInterface):
    @abstractmethod
    def get_by_username(self, username):
        raise NotImplemented


class UserServiceInterface(CrudInterface, ABC): ...
