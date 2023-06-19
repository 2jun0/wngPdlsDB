from dataclasses import dataclass
from wngPdlsDB.dto import ArtistDto, AlbumDto


@dataclass
class SongDto:
    genie_id: str
    title: str
    artist: ArtistDto
    album: AlbumDto
