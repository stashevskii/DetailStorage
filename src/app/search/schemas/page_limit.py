from pydantic import Field
from src.app.search.core.common.schema import BaseSchema


class PageLimitSchema(BaseSchema):
    page_limit: int = Field(ge=1)