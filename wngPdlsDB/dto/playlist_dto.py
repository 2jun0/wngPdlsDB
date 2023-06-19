from dataclasses import dataclass
from wngPdlsDB.dto.tag_dto import TagDto


@dataclass
class PlaylistDto:
    id: str
    genie_id: int
    title: str
    description: str
    likes: int
    views: int
    tags: list[TagDto]
