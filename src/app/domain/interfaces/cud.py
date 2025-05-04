from abc import ABC, abstractmethod


class CudInterface(ABC):  # Cud (not crud) because no reading/getting method
    @abstractmethod
    def add(self, schema):
        raise NotImplemented

    @abstractmethod
    def delete(self, id):
        raise NotImplemented

    @abstractmethod
    def full_update(self, id, schema):
        raise NotImplemented

    @abstractmethod
    def part_update(self, id, update_params):
        raise NotImplemented
