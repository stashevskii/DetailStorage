from abc import ABC, abstractmethod


class CrudInterface(ABC):
    @abstractmethod
    def get(self, schema):
        raise NotImplemented

    @abstractmethod
    def add(self, schema):
        raise NotImplemented

    @abstractmethod
    def delete(self, id):
        raise NotImplemented

    @abstractmethod
    def full_update(self, id, schema):  # put http request
        raise NotImplemented

    @abstractmethod
    def part_update(self, id, schema):  # patch http request
        raise NotImplemented
