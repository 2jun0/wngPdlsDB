from mongoengine import (
    Document,
    StringField,
    IntField,
    ListField,
    ReferenceField,
    ValidationError,
)
from wngPdlsDB.dto import PlaylistDto
from wngPdlsDB.document.tag_document import TagDocument
from wngPdlsDB.document.song_document import SongDocument


def should_have_at_least_one_tag(tags: list[TagDocument]):
    if len(tags) <= 0:
        raise ValidationError("Playlist should have at least one tags")


def should_have_at_least_one_song(songs: list[SongDocument]):
    if len(songs) <= 0:
        raise ValidationError("Playlist should have at least one songs")


class PlaylistDocument(Document):
    genie_id = StringField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    likes = IntField(required=True)
    views = IntField(required=True)
    tags = ListField(
        ReferenceField(TagDocument),
        required=True,
        validation=should_have_at_least_one_tag,
    )
    songs = ListField(
        ReferenceField(SongDocument),
        required=True,
        validation=should_have_at_least_one_song,
    )

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
