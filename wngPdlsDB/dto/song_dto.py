from dataclasses import dataclass


@dataclass
class SongDto:
    genie_id: str
    title: str
    artist: str
    album: str
