from dataclasses import dataclass
from wngPdlsDB.dto.tag_dto import TagDto
from wngPdlsDB.dto.song_dto import SongDto


@dataclass
class PlaylistDto:
    id: str
    genie_id: str
    title: str
    description: str
    likes: int
    views: int
    tags: list[TagDto]
    songs: list[SongDto]
