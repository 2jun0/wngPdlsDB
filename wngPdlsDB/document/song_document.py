from mongoengine import Document, StringField, ReferenceField
from wngPdlsDB.dto import SongDto
from wngPdlsDB.document.artist_document import ArtistDocument
from wngPdlsDB.document.album_document import AlbumDocument


class SongDocument(Document):
    genie_id = StringField(required=True, unique=True)
    title = StringField(required=True)
    artist = ReferenceField(ArtistDocument, required=True)
    album = ReferenceField(AlbumDocument, required=True)

    def to_dto(self) -> SongDto:
        return SongDto(
            str(self.id),
            self.genie_id,
            self.title,
            self.artist.to_dto(),
            self.album.to_dto(),
        )
