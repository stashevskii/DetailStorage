class AuthRouterConfig:
    prefix: str = "/api/auth"
    tags: list[str] = ["Auth"]
    docs: dict = {
        1: {
            "summary": "Login",
            "description": "Login endpoint"
        }
    }
