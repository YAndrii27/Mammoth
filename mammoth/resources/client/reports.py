from __future__ import annotations
from typing import TYPE_CHECKING, cast

from ...session import Session

if TYPE_CHECKING:
    from ...client import MastodonClient
from .base import BaseClientResource

from ...utils import version
from ...enums import HttpMethods, ReportCategory
from ...models import Report


class Reports(BaseClientResource):

    def __init__(self: Reports, client: "MastodonClient"):
        super().__init__(client=client)

    @version(version="v1")
    async def file_report(
        self: Reports,
        account_id: str,
        status_ids: list[str] | None,
        comment: str | None,
        forward: bool | None,
        category: ReportCategory | str | None,
        rule_ids: list[str] | None
    ) -> Report:
        if isinstance(category, ReportCategory):
            category = category.value

        session: Session[Report | None] = await self.client(
            http_method=HttpMethods.POST,
            scope="reports",
            expected_type=Report,
            method="",
            post_data={
                "account_id": account_id,
                "status_ids": status_ids,
                "comment": comment,
                "forward": forward,
                "category": category,
                "rule_ids": rule_ids
            },
            response_is_list=False
        )
        return cast(Report, await session())
