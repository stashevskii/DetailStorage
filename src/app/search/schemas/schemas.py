from pydantic import Field, field_validator, ValidationError
from src.app.search.core.common.schema import BaseSchema


class PageLimitSchema(BaseSchema):
    page_limit: int = Field(ge=1)


class GetDetailByLegoIdSchema(PageLimitSchema):
    lego_id: int = Field(ge=0)


class GetDetailByNameSchema(PageLimitSchema):
    name: str = Field(min_length=1)
