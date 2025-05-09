from abc import abstractmethod, ABC
from .crud import CrudInterface


class UserRepositoryInterface(CrudInterface):
    @abstractmethod
    def get_all(self):
        raise NotImplemented


class UserServiceInterface(CrudInterface, ABC): ...
