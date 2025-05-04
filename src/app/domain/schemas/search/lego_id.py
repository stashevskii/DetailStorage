from pydantic import Field
from .page_limit import PageLimitSchema


class GetDetailByLegoIdSchema(PageLimitSchema):
    lego_id: int = Field(ge=0)
