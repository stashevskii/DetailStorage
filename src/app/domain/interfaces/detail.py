from abc import abstractmethod, ABC
from .cud import CudInterface


class DetailRepositoryInterface(CudInterface):
    @abstractmethod
    def get(self, filter_params, all_obj):
        raise NotImplemented


class DetailServiceInterface(CudInterface):
    @abstractmethod
    def get(self, schema):
        raise NotImplemented
