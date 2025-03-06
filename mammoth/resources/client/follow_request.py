from __future__ import annotations
from typing import TYPE_CHECKING, cast

from ...session import Session

if TYPE_CHECKING:
    from ...client import MastodonClient
from .base import BaseClientResource

from ...utils import version
from ...enums import HttpMethods
from ...models import Account, Relationship


class FollowRequests(BaseClientResource):

    def __init__(self: FollowRequests, client: "MastodonClient"):
        super().__init__(client=client)

    @version(version="v1")
    async def get_follow_requests(
        self: FollowRequests,
        limit: int,
    ) -> list[Account]:

        session: Session[Account | None] = await self.client(
            http_method=HttpMethods.POST,
            scope="follow_requests",
            expected_type=Account,
            method="",
            query_parameters={
                "limit": limit,
            },
            response_is_list=True
        )
        return cast(list[Account], await session())

    @version(version="v1")
    async def accept_follow_request(
        self: FollowRequests,
        account_id: str,
    ) -> Relationship:

        session: Session[Relationship | None] = await self.client(
            http_method=HttpMethods.POST,
            scope="follow_requests",
            expected_type=Relationship,
            url_parameters=(account_id,),
            method="authorize",
            response_is_list=True
        )
        return cast(Relationship, await session())
    
    @version(version="v1")
    async def reject_follow_request(
        self: FollowRequests,
        account_id: str,
    ) -> Relationship:

        session: Session[Relationship | None] = await self.client(
            http_method=HttpMethods.POST,
            scope="follow_requests",
            expected_type=Relationship,
            url_parameters=(account_id,),
            method="reject",
            response_is_list=True
        )
        return cast(Relationship, await session())
