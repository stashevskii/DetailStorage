class AdminRouterConfig:
    prefix: str = "/api/admin"
    tags = ["Admin"]
    docs: dict = {
        1: {
            "summary": "Get all users (only for admin)",
            "description": "Get all users (only for admin) endpoint"
        },
        2: {
            "summary": "Add new user (only for admin)",
            "description": "Add new user (only for admin) endpoint"
        },
        3: {
            "summary": "Delete any user (only for admin)",
            "description": "Delete any user (only for admin) endpoint"
        },
        4: {
            "summary": "Full update user (only for admin)",
            "description": "Full update user (only for admin) endpoint"
        },
        5: {
            "summary": "Part update user (only for admin)",
            "description": "Part update user (only for admin) endpoint"
        }
    }
