from __future__ import annotations
from typing import cast

from mammoth.session import Session

from .base import BaseClientResource
from ...client import MastodonClient
from ...models import Status
from ...utils import version
from ...enums import HttpMethods


class Favourites(BaseClientResource):
    def __init__(self, client: MastodonClient) -> None:
        super().__init__(client=client)

    @version(version="v1")
    async def favourites(
        self: BaseClientResource,
        limit: int
    ) -> list[Status]:
        session: Session[Status | None] = await self.client(
            http_method=HttpMethods.GET,
            scope="favourites",
            expected_type=Status,
            response_is_list=True,
            query_parameters={
                "limit": limit
            }
        )
        return cast(list[Status], await session())
