class AuthRouterConfig:
    prefix: str = "/api/auth"
    tags: list[str] = ["Auth"]
    docs: dict[int: dict[str: str]] = {
        1: {
            "summary": "Login",
            "description": "Login endpoint"
        }
    }
