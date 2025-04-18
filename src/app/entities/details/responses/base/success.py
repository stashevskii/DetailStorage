from src.app.entities.base import DetailStorageBase


class SuccessResponseModel(DetailStorageBase):
    success: bool = None
