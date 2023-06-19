from dataclasses import dataclass
from wngPdlsDB.dto.artist_dto import ArtistDto
from wngPdlsDB.dto.album_dto import AlbumDto


@dataclass
class SongDto:
    id: str
    genie_id: str
    title: str
    artist: ArtistDto
    album: AlbumDto
