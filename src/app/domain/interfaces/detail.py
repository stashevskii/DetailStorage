from abc import ABC, abstractmethod
from .crud import CrudInterface


class DetailRepositoryInterface(CrudInterface):
    @abstractmethod
    def get_all(self):
        raise NotImplemented


class DetailServiceInterface(CrudInterface, ABC): ...
