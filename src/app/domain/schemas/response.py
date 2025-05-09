from pydantic import Field
from src.app.core.base import BaseSchema


class SuccessSchema(BaseSchema):
    success: bool = Field()
