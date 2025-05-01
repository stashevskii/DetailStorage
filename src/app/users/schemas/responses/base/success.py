from src.app.users.core.common.schema import BaseSchema


class SuccessResponseSchema(BaseSchema):
    success: bool = None
