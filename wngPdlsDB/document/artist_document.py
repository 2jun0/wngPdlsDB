from mongoengine import Document, StringField
from dto.tag_dto import ArtistDto


class ArtistDocument(Document):
    genie_id = StringField(required=True, unique=True)
    name = StringField(required=True, unique=True)

    def to_dto(self) -> ArtistDto:
        return ArtistDto(self.genie_id, self.name)
