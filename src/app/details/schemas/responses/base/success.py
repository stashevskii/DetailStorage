from src.app.bases.base_schema import BaseSchema


class SuccessResponseSchema(BaseSchema):
    success: bool = None
