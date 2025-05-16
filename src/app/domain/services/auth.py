from fastapi.security import HTTPBasicCredentials
from src.app.core.base import Service
from src.app.core.utils import compare_passwords
from src.app.core.utils.password import get_bytes_from_db_hex_hash
from src.app.domain.abstractions import UserRepositoryInterface
from src.app.domain.abstractions.auth import AuthServiceInterface
from src.app.domain.exceptions.auth import InvalidCredentialsException


class AuthService(Service, AuthServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        super().__init__(user_repository)

    def login(self, credentials: HTTPBasicCredentials) -> dict[str: str]:
        user = self.repository.get_by_username(credentials.username)
        if not user or not compare_passwords(credentials.password, get_bytes_from_db_hex_hash(user.hashed_password)):
            raise InvalidCredentialsException
        return {"message": f"Successful login", "user": user}
