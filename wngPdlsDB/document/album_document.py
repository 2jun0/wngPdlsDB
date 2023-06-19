from mongoengine import Document, StringField
from wngPdlsDB.dto import AlbumDto


class AlbumDocument(Document):
    genie_id = StringField(required=True, unique=True)
    title = StringField(required=True)

    def to_dto(self) -> AlbumDto:
        return AlbumDto(self.genie_id, self.title)
