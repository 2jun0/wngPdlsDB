from wngPdlsDB.document import SongDocument, ArtistDocument, AlbumDocument
from wngPdlsDB.dto import SongDto, ArtistDto, AlbumDto


class SongRepository:
    def create_song(
        self,
        genie_id: str,
        title: str,
        artist: ArtistDto,
        album: AlbumDto
    ) -> SongDto:
        song = SongDocument(
            genie_id=genie_id,
            title=title,
            artist=self.__find_artist_doc_by_dto(artist),
            album=self.__find_album_doc_by_dto(album)
            )
        saved: SongDocument = song.save()
        return saved.to_dto()

    def delete_song(self, genie_id: str) -> None:
        self.find_by_genie_id(genie_id).delete()

    def find_by_genie_id(self, genie_id: str) -> SongDto:
        song: SongDocument = SongDocument.objects(genie_id=genie_id).first()
        return song.to_dto()

    def find_by_artist(self, artist: ArtistDto) -> list[SongDto]:
        artist_doc: ArtistDocument = self.__find_artist_doc_by_dto(artist)
        songs: list[SongDocument] = SongDocument.objects(artist=artist_doc)
        return [song.to_dto() for song in songs]

    def find_by_album(self, album: AlbumDto) -> list[SongDto]:
        album_doc: AlbumDocument = self.__find_album_doc_by_dto(album)
        songs: list[SongDocument] = SongDocument.objects(album=album_doc)
        return [song.to_dto() for song in songs]

    def find_all(self) -> list[SongDto]:
        songs: list[SongDocument] = list(SongDocument.objects)
        return [song.to_dto() for song in songs]

    def __find_artist_doc_by_dto(self, artist: ArtistDto) -> ArtistDocument:
        return ArtistDocument.objects(genie_id=artist.genie_id).first()

    def __find_album_doc_by_dto(self, album: AlbumDto) -> AlbumDocument:
        return AlbumDocument.objects(genie_id=album.genie_id).first()
