from dataclasses import dataclass
from datetime import datetime


@dataclass
class PlaylistDto:
    genie_id: int
    title: str
    description: str
    likes: int
    views: int
    created_date: datetime
    updated_date: datetime
