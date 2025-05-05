class SearchRouterConfig:
    prefix: str = "/api/details"
    tags: list[str] = ["Search details"]
    docs: dict[int: dict[str: str]] = {
        1: {
            "summary": "Get detail by lego id (parsing lego.com)",
            "description": "Get detail by lego id (parsing lego.com) endpoint"
        },
        2: {
            "summary": "Get detail by name (parsing lego.com)",
            "description": "Get detail by name (parsing lego.com) endpoint"
        },
    }
