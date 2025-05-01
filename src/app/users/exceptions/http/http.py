from fastapi import status, HTTPException


class NotFoundUserHttpException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
            headers=None
        )


class UserAlreadyExistsHttpException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
            headers=None
        )


class UserWithThisEmailAlreadyExistsHttpException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
            headers=None
        )
