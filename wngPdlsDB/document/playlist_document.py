from mongoengine import Document, StringField, IntField, DateTimeField
from wngPdlsDB.dto import PlaylistDto


class PlaylistDocument(Document):
    genie_id = IntField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    likes = IntField(required=True)
    views = IntField(required=True)
    created_date = DateTimeField(required=True)
    updated_date = DateTimeField(required=True)

    def to_dto(self) -> PlaylistDto:
        return PlaylistDto(
            self.genie_id,
            self.title,
            self.description,
            self.likes,
            self.views,
            self.created_date,
            self.updated_date,
        )
