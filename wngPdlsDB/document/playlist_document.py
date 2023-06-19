from mongoengine import (
    Document,
    StringField,
    IntField,
    ListField,
    ReferenceField,
)
from wngPdlsDB.dto import PlaylistDto
from wngPdlsDB.document.tag_document import TagDocument
from wngPdlsDB.document.song_document import SongDocument


class PlaylistDocument(Document):
    genie_id = IntField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    likes = IntField(required=True)
    views = IntField(required=True)
    tags = ListField(ReferenceField(TagDocument), required=True)
    songs = ListField(ReferenceField(SongDocument))

    def to_dto(self) -> PlaylistDto:
        return PlaylistDto(
            str(self.id),
            self.genie_id,
            self.title,
            self.description,
            self.likes,
            self.views,
            [tag.to_dto() for tag in self.tags],
            [song.to_dto() for song in self.songs],
        )
