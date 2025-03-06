from __future__ import annotations
from typing import TYPE_CHECKING, cast

from ...session import Session

if TYPE_CHECKING:
    from ...client import MastodonClient
from .base import BaseClientResource

from ...utils import version
from ...enums import HttpMethods
from ...models import Account


class Endorsements(BaseClientResource):

    def __init__(self: Endorsements, client: "MastodonClient"):
        super().__init__(client=client)

    @version(version="v1")
    async def get_endorsements(
        self: Endorsements,
        limit: int,
    ) -> list[Account]:

        session: Session[Account | None] = await self.client(
            http_method=HttpMethods.POST,
            scope="endorsements",
            expected_type=Account,
            method="",
            query_parameters={
                "limit": limit,
            },
            response_is_list=True
        )
        return cast(list[Account], await session())
