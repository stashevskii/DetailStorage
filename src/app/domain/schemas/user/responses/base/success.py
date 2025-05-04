from src.app.core.common.schema import BaseSchema


class SuccessResponseSchema(BaseSchema):
    success: bool = None
