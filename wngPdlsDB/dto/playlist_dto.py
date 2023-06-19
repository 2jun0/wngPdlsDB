from dataclasses import dataclass
from datetime import datetime
from wngPdlsDB.dto import TagDto


@dataclass
class PlaylistDto:
    id: str
    genie_id: int
    title: str
    description: str
    likes: int
    views: int
    created_date: datetime
    updated_date: datetime
    tags: list[TagDto]
