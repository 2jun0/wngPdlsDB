from mongoengine import (
    Document,
    StringField,
    IntField,
    DateTimeField,
    ListField,
    ReferenceField,
)
from wngPdlsDB.dto import PlaylistDto
from wngPdlsDB.document.tag_document import TagDocument


class PlaylistDocument(Document):
    genie_id = IntField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    likes = IntField(required=True)
    views = IntField(required=True)
    created_date = DateTimeField(required=True)
    updated_date = DateTimeField(required=True)
    tags = ListField(ReferenceField(TagDocument), required=True)

    def to_dto(self) -> PlaylistDto:
        return PlaylistDto(
            self.id.toString(),
            self.genie_id,
            self.title,
            self.description,
            self.likes,
            self.views,
            self.created_date,
            self.updated_date,
            [tag.to_dto() for tag in self.tags],
        )
