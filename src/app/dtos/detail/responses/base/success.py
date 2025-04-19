from src.app.dtos.base import DetailStorageBase


class SuccessResponseDto(DetailStorageBase):
    success: bool = None
