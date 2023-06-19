from mongoengine import Document, StringField
from dto.tag_dto import TagDto


class TagDocument(Document):
    genie_id = StringField(required=True, unique=True)
    title = StringField(required=True, unique=True)

    def to_dto(self) -> TagDto:
        return TagDto(self.genie_id, self.title)
