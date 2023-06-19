from mongoengine import Document, StringField, ReferenceField
from wngPdlsDB.dto import SongDto
from wngPdlsDB.document import ArtistDocument , AlbumDocument


class SongDocument(Document):
    genie_id = StringField(required=True, unique=True)
    title = StringField(required=True)
    artist = ReferenceField(ArtistDocument, required=True)
    album = ReferenceField(AlbumDocument, required=True)

    def to_dto(self) -> SongDto:
        return SongDto(
            self.genie_id,
            self.title,
            self.artist.to_dto(),
            self.album.to_dto(),
        )
