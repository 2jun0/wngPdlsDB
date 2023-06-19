from wngPdlsDB.document import PlaylistDocument
from wngPdlsDB.dto import PlaylistDto


class PlaylistRepository:
    def create_playlist(
        self,
        genie_id: int,
        title: str,
        description: str,
        likes: int,
        views: int,
        created_date,
        updated_date,
    ) -> PlaylistDto:
        playlist = PlaylistDocument(
            genie_id=genie_id,
            title=title,
            description=description,
            likes=likes,
            views=views,
            created_date=created_date,
            updated_date=updated_date,
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
