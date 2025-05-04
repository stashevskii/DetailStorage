from abc import abstractmethod
from .cud import CudInterface


class UserRepositoryInterface(CudInterface):
    @abstractmethod
    def get(self, filter_params: dict, all_obj: bool) -> dict:
        raise NotImplemented


class UserServiceInterface(CudInterface):
    @abstractmethod
    def get(self, schema):
        raise NotImplemented
