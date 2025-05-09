from abc import ABC
from .basic import CrudInterface, GetAllInterface


class UserRepositoryInterface(CrudInterface, GetAllInterface, ABC): ...


class UserServiceInterface(CrudInterface, ABC): ...
