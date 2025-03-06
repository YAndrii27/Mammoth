from pydantic import BaseModel
from datetime import datetime


class Report(BaseModel):
    id: str
    action_taken: bool
    action_taken_at: datetime | None
    category: str
    pass
