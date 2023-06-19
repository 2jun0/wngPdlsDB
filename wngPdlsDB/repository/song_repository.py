from wngPdlsDB.document import SongDocument, ArtistDocument, AlbumDocument
from wngPdlsDB.dto import SongDto, ArtistDto, AlbumDto
from wngPdlsDB.exception import (
    NotFoundSongException,
    NotFoundAlbumException,
    NotFoundArtistException,
)


class SongRepository:
    def create_song(
        self, genie_id: str, title: str, artist: ArtistDto, album: AlbumDto
    ) -> SongDto:
        song = SongDocument(
            genie_id=genie_id,
            title=title,
            artist=self.__find_artist_doc_by_dto(artist),
            album=self.__find_album_doc_by_dto(album),
        )
        saved: SongDocument = song.save()
        return saved.to_dto()

    def delete_by_genie_id(self, genie_id: str) -> None:
        query_set = SongDocument.objects(genie_id=genie_id)

        if not query_set:
            raise NotFoundSongException(
                f"Can't find song document: genie_id={genie_id}"
            )

        query_set.delete()

    def find_by_genie_id(self, genie_id: str) -> SongDto | None:
        song: SongDocument = SongDocument.objects(genie_id=genie_id).first()

        if not song:
            return None

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
        artist = ArtistDocument.objects(genie_id=artist.genie_id).first()

        if not artist:
            raise NotFoundArtistException(f"Can't find artist document: {artist}")

        return artist

    def __find_album_doc_by_dto(self, album: AlbumDto) -> AlbumDocument:
        album = AlbumDocument.objects(genie_id=album.genie_id).first()

        if not album:
            raise NotFoundAlbumException(f"Can't find album document: {album}")

        return album
