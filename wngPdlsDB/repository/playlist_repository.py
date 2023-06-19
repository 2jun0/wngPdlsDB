from mongoengine import QuerySet
from wngPdlsDB.document import PlaylistDocument, TagDocument
from wngPdlsDB.dto import PlaylistDto, TagDto


class PlaylistRepository:
    def create_playlist(
        self,
        genie_id: int,
        title: str,
        description: str,
        likes: int,
        views: int,
        tags: list[TagDto],
    ) -> PlaylistDto:
        playlist = PlaylistDocument(
            genie_id=genie_id,
            title=title,
            description=description,
            likes=likes,
            views=views,
            tags=self.__find_tags_doc_by_dto(tags),
        )
        saved: PlaylistDocument = playlist.save()
        return saved.to_dto()

    def delete_playlist(self, genie_id: str) -> None:
        self.find_by_genie_id(genie_id).delete()

    def find_by_genie_id(self, genie_id: str) -> PlaylistDto:
        playlist: PlaylistDocument = PlaylistDocument.objects(genie_id=genie_id).first()
        return playlist.to_dto()

    def find_all(self) -> list[PlaylistDto]:
        playlists: list[PlaylistDocument] = list(PlaylistDocument.objects)
        return [playlist.to_dto() for playlist in playlists]

    def find_by_tag(self, tag: TagDto) -> list[PlaylistDto]:
        tag_doc = self.__find_tag_doc_by_dto(tag)
        playlist: PlaylistDocument = PlaylistDocument.objects(tag=tag_doc).first()
        return playlist.to_dto()

    def __find_tag_doc_by_dto(self, tag: TagDto) -> TagDocument:
        return TagDocument.objects(genie_id=tag.genie_id).first()

    def __find_tags_doc_by_dto(self, tags: list[TagDto]) -> QuerySet:
        tag_genie_ids = [tag.genie_id for tag in tags]
        return TagDocument.objects(genie_id__in=tag_genie_ids)
