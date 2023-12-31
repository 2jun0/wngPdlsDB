from mongoengine import Document, StringField
from wngPdlsDB.dto import ArtistDto


class ArtistDocument(Document):
    genie_id = StringField(required=True, unique=True)
    name = StringField(required=True)

    def to_dto(self) -> ArtistDto:
        return ArtistDto(str(self.id), self.genie_id, self.name)
