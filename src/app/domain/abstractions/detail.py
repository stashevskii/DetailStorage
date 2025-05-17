from abc import ABC, abstractmethod
from .basic import CrudInterface, GetAllInterface


class Repeated(ABC):
    @abstractmethod
    def delete(self, id, user_id):
        raise NotImplemented

    @abstractmethod
    def replace(self, id, user_id, schema):
        raise NotImplemented

    @abstractmethod
    def part_update(self, id, user_id, schema):
        raise NotImplemented


class DetailRepositoryInterface(GetAllInterface, Repeated, ABC):
    @abstractmethod
    def get(self, **kwargs):
        raise NotImplemented

    @abstractmethod
    def add(self, **kwargs):
        raise NotImplemented


class DetailServiceInterface(Repeated, ABC):
    @abstractmethod
    def get(self, user_id, schema):
        raise NotImplemented

    @abstractmethod
    def add(self, user_id, schema):
        raise NotImplemented
