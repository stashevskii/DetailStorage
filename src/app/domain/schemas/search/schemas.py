from pydantic import Field
from src.app.core.base.schema import BaseSchema


class PageLimitSchema(BaseSchema):
    page_limit: int = Field(ge=1, le=15)


class DetailName(PageLimitSchema):
    name: str = Field(min_length=1)


class DetailLegoId(PageLimitSchema):
    lego_id: int = Field(ge=0)
