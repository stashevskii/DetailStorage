from pydantic import Field
from src.app.core.base.schema import BaseSchema


class SuccessSchema(BaseSchema):
    success: bool = Field()
