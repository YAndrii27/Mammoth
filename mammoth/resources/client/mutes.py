from __future__ import annotations
from typing import cast

from mammoth.session import Session

from .base import BaseClientResource
from ...client import MastodonClient
from ...models import Account
from ...utils import version
from ...enums import HttpMethods


class Mutes(BaseClientResource):
    def __init__(self, client: MastodonClient) -> None:
        super().__init__(client=client)

    @version(version="v1")
    async def mutes(
        self: BaseClientResource,
        limit: int
    ) -> list[Account]:
        session: Session[Account | None] = await self.client(
            http_method=HttpMethods.GET,
            scope="mutes",
            expected_type=Account,
            response_is_list=True,
            query_parameters={
                "limit": limit
            }
        )
        return cast(list[Account], await session())
