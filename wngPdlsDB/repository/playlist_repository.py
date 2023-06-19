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
