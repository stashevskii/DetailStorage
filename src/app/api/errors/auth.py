from fastapi import HTTPException
from fastapi import status


class InvalidPasswordOrUsernameHttpError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password or username",
            headers={"WWW-Authenticate": "Basic"}
        )


class UnauthedHttpError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Current user is not authed",
            # headers={"WWW-Authenticate": "Basic"}
        )
