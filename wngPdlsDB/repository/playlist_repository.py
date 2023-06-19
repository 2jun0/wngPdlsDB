from wngPdlsDB.document import PlaylistDocument


class PlaylistRepository:
    def create_playlist(
        genie_id: int,
        title: str,
        description: str,
        likes: int,
        views: int,
        created_date,
        updated_date,
    ):
        playlist = PlaylistDocument(
            genie_id=genie_id,
            title=title,
            description=description,
            likes=likes,
            views=views,
            created_date=created_date,
            updated_date=updated_date,
        )
        playlist.save()
