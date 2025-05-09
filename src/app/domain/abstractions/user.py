from abc import ABC
from .basic import CrudInterface, GetAllInterface, GetByIdInterface


class UserRepositoryInterface(CrudInterface, GetAllInterface, GetByIdInterface, ABC): ...


class UserServiceInterface(CrudInterface, GetByIdInterface, ABC): ...
