from fastapi import HTTPException
from fastapi import status


class InvalidCredentialsHttp(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password or username",
            headers={"WWW-Authenticate": "Basic"}
        )


class UnauthedHttp(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are unauthorized",
            headers={"WWW-Authenticate": ""}
        )
