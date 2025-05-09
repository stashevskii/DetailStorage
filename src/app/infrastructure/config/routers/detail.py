class DetailRouterConfig:
    prefix: str = "/api/details"
    tags: list[str] = ["Details"]
    docs: dict[int: dict[str: str]] = {
        1: {
            "summary": "Get details by parameters",
            "description": "Get details by parameters endpoint"
        },
        2: {
            "summary": "Add new detail",
            "description": "Add new detail endpoint"
        },
        3: {
            "summary": "Delete detail",
            "description": "Delete detail endpoint"
        },
        4: {
            "summary": "Full update detail",
            "description": "Full update detail endpoint"
        },
        5: {
            "summary": "Part update detail",
            "description": "Part update detail endpoint"
        }
    }
