from mongoengine import Document, StringField
from dto.song_dto import SongDto


class SongDocument(Document):
    genie_id = StringField(required=True, unique=True)
    title = StringField(required=True, unique=True)
    artist = StringField(required=True, unique=False) #TODO: unique
    album = StringField(required=True, unique=True)
    

    def to_dto(self) -> SongDto:
        return SongDto(
            self.genie_id,
            self.title,
            self.artist,
            self.album,
            )
