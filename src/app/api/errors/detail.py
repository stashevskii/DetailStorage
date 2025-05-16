from fastapi import status, HTTPException


class NotFoundDetailHttp(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Detail not found",
            headers=None
        )


class DetailAlreadyExistsHttp(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Detail already exists",
            headers=None
        )
