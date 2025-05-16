class UserRouterConfig:
    prefix: str = "/api/users"
    tags: list[str] = ["Users"]
    docs: dict = {
        1: {
            "summary": "Get current user",
            "description": "Get current user endpoint"
        },
        2: {
            "summary": "Delete current user",
            "description": "Delete current user endpoint"
        },
        3: {
            "summary": "Full update current user",
            "description": "Full update current user endpoint"
        },
        4: {
            "summary": "Part update current user",
            "description": "Part update current user endpoint"
        },
    }
