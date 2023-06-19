from wngPdlsDB.document import SongDocument
from wngPdlsDB.document import SongDto


class SongRepository:
    def create_song(self, genie_id: str, title: str, artist: str, album: str) -> SongDto:
        song = SongDocument(genie_id=genie_id, title=title, artist=artist, album=album)
        saved: SongDocument = song.save()
        return saved.to_dto()

    def delete_song(self, genie_id: str) -> None:
        self.find_by_genie_id(genie_id).delete()

    def find_by_genie_id(self, genie_id: str) -> SongDto:
        song: SongDocument = SongDocument.objects(genie_id=genie_id).first()
        return song.to_dto()

    def find_all(self) -> list[SongDto]:
        songs: list[SongDocument] = list(SongDocument.objects)
        return [song.to_dto() for song in songs]
