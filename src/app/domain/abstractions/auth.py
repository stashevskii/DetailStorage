from abc import ABC, abstractmethod


class AuthServiceInterface(ABC):
    @abstractmethod
    def login(self, credentials):
        raise NotImplemented
