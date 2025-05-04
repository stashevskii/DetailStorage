from pydantic import Field
from .page_limit import PageLimitSchema


class GetDetailByNameSchema(PageLimitSchema):
    name: str = Field(min_length=1)
