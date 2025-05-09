from abc import ABC
from .basic import CrudInterface, GetAllInterface


class DetailRepositoryInterface(CrudInterface, GetAllInterface, ABC): ...


class DetailServiceInterface(CrudInterface, ABC): ...
