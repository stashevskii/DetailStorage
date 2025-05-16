from fastapi import HTTPException
from fastapi import status


class NotFoundUserHttp(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
            headers=None
        )


class UserAlreadyExistsHttp(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
            headers=None
        )


class DuplicateEmailHttp(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
            headers=None
        )


class DuplicateUsernameHttp(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists",
            headers=None
        )
