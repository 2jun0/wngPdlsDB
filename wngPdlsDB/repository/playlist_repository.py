from mongoengine import QuerySet
from wngPdlsDB.document import PlaylistDocument, TagDocument, SongDocument
from wngPdlsDB.dto import PlaylistDto, TagDto, SongDto
from wngPdlsDB.exception import (
    NotFoundPlaylistException,
    NotFoundTagException,
    NotFoundSongException,
)


class PlaylistRepository:
    def create_playlist(
        self,
        genie_id: str,
        title: str,
        description: str,
        likes: int,
        views: int,
        tags: list[TagDto],
        songs: list[SongDto],
    ) -> PlaylistDto:
        playlist = PlaylistDocument(
            genie_id=genie_id,
            title=title,
            description=description,
            likes=likes,
            views=views,
            tags=self.__find_tag_docs_by_dto(tags),
            songs=self.__find_song_docs_by_dto(songs),
        )
        saved: PlaylistDocument = playlist.save()
        return saved.to_dto()

    def delete_by_genie_id(self, genie_id: str) -> None:
        query_set = PlaylistDocument.objects(genie_id=genie_id)

        if not query_set:
            raise NotFoundPlaylistException(
                f"Can't find playlist document: genie_id={genie_id}"
            )

        query_set.delete()

    def find_by_genie_id(self, genie_id: str) -> PlaylistDto | None:
        playlist: PlaylistDocument = PlaylistDocument.objects(genie_id=genie_id).first()

        if not playlist:
            return None

        return playlist.to_dto()

    def find_all(self) -> list[PlaylistDto]:
        playlists: list[PlaylistDocument] = list(PlaylistDocument.objects)
        return [playlist.to_dto() for playlist in playlists]

    def find_by_tag(self, tag: TagDto) -> list[PlaylistDto]:
        tag_doc = self.__find_tag_doc_by_dto(tag)
        playlists: list[PlaylistDocument] = list(PlaylistDocument.objects(tags=tag_doc))
        return [playlist.to_dto() for playlist in playlists]

    def find_by_song(self, song: SongDto) -> list[SongDto]:
        song_doc = self.__find_song_doc_by_dto(song)
        playlists: list[PlaylistDocument] = list(
            PlaylistDocument.objects(songs=song_doc)
        )
        return [playlist.to_dto() for playlist in playlists]

    def __find_tag_doc_by_dto(self, tag: TagDto) -> TagDocument:
        query_set = TagDocument.objects(genie_id=tag.genie_id)

        if not query_set:
            raise NotFoundTagException(f"Can't find tag document: {tag}")

        return query_set.first()

    def __find_tag_docs_by_dto(self, tags: list[TagDto]) -> QuerySet:
        tag_genie_ids = [tag.genie_id for tag in tags]
        query_set = TagDocument.objects(genie_id__in=tag_genie_ids)

        if tags and not query_set:
            raise NotFoundTagException(f"Can't find tag documents: {tags}")

        return query_set

    def __find_song_doc_by_dto(self, song: SongDto) -> SongDocument:
        query_set = SongDocument.objects(genie_id=song.genie_id)

        if not query_set:
            raise NotFoundSongException(f"Can't find song document: {song}")

        return query_set.first()

    def __find_song_docs_by_dto(self, songs: list[SongDto]) -> QuerySet:
        songs_genie_ids = [songs.genie_id for songs in songs]
        query_set = SongDocument.objects(genie_id__in=songs_genie_ids)

        if songs and not query_set:
            raise NotFoundSongException(f"Can't find song documents: {songs}")

        return query_set
