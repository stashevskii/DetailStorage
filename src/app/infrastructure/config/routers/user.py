class UserRouterConfig:
    prefix: str = "/api/users"
    tags: list[str] = ["Users"]
    docs: dict[int: dict[str: str]] = {
        1: {
            "summary": "Get user by parameters",
            "description": "Get user by parameters endpoint"
        },
        2: {
            "summary": "Add new user",
            "description": "Add new user endpoint"
        },
        3: {
            "summary": "Delete user",
            "description": "Delete user endpoint"
        },
        4: {
            "summary": "Full update user",
            "description": "Full update user endpoint"
        },
        5: {
            "summary": "Part update user",
            "description": "Part update user endpoint"
        },
        6: {
            "summary": "Get all users",
            "description": "Get all users endpoint"
        }
    }
