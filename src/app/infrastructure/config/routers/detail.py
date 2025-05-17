class DetailRouterConfig:
    prefix: str = "/api/details"
    tags: list[str] = ["Details"]
    docs: dict = {
        1: {
            "summary": "Get details by parameters (connected to current authed user)",
            "description": "Get details by parameters (connected to current authed user) endpoint"
        },
        2: {
            "summary": "Add new detail (connected to current authed user)",
            "description": "Add new detail (connected to current authed user) endpoint"
        },
        3: {
            "summary": "Delete detail (connected to current authed user)",
            "description": "Delete detail (connected to current authed user) endpoint"
        },
        4: {
            "summary": "Full update detail (connected to current authed user)",
            "description": "Full update detail (connected to current authed user) endpoint"
        },
        5: {
            "summary": "Part update detail (connected to current authed user)",
            "description": "Part update detail (connected to current authed user) endpoint"
        }
    }
