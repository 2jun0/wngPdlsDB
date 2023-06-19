from mongoengine import Document, StringField
from wngPdlsDB.dto import SongDto


class SongDocument(Document):
    genie_id = StringField(required=True, unique=True)
    title = StringField(required=True)
    artist = StringField(required=True)
    album = StringField(required=True)

    def to_dto(self) -> SongDto:
        return SongDto(
            self.genie_id,
            self.title,
            self.artist,
            self.album,
        )
