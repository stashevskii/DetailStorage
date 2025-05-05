class DetailRouterConfig:
    prefix: str = "/api/details"
    tags: list[str] = ["Details"]
    docs: dict[int: dict[str: str]] = {
        1: {
            "summary": "Get details by parameters",
            "description": "Get details by parameters endpoint"
        },
        2: {
            "summary": "Add new details",
            "description": "Add new details endpoint"
        },
        3: {
            "summary": "Delete details",
            "description": "Delete details endpoint"
        },
        4: {
            "summary": "Full update details",
            "description": "Full update details endpoint"
        },
        5: {
            "summary": "Part update details",
            "description": "Part update details endpoint"
        }
    }
