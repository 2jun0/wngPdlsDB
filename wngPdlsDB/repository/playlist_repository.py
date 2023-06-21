from wngPdlsDB.document import PlaylistDocument
from wngPdlsDB.dto import PlaylistDto, TagDto, SongDto
from wngPdlsDB.exception import (
    NotFoundPlaylistException,
)
from wngPdlsDB.repository.common import (
    _find_tag_docs_by_dto,
    _find_song_docs_by_dto,
    _find_tag_doc_by_dto,
    _find_song_doc_by_dto,
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
            tags=_find_tag_docs_by_dto(tags),
            songs=_find_song_docs_by_dto(songs),
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
        tag_doc = _find_tag_doc_by_dto(tag)
        playlists: list[PlaylistDocument] = list(PlaylistDocument.objects(tags=tag_doc))
        return [playlist.to_dto() for playlist in playlists]

    def find_by_song(self, song: SongDto) -> list[SongDto]:
        song_doc = _find_song_doc_by_dto(song)
        playlists: list[PlaylistDocument] = list(
            PlaylistDocument.objects(songs=song_doc)
        )
        return [playlist.to_dto() for playlist in playlists]
