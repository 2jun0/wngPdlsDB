from wngPdlsDB.document import AlbumDocument
from wngPdlsDB.exception import NotFoundAlbumException
from wngPdlsDB.dto import AlbumDto


class AlbumRepository:
    def create_album(self, genie_id: str, title: str) -> AlbumDto:
        album = AlbumDocument(genie_id=genie_id, title=title)
        saved: AlbumDocument = album.save()
        return saved.to_dto()

    def delete_by_genie_id(self, genie_id: str) -> None:
        album: AlbumDocument = AlbumDocument.objects(genie_id=genie_id).first()

        if not album:
            raise NotFoundAlbumException(
                f"Can't find album document: genie_id={genie_id}"
            )

        album.delete()

    def find_by_genie_id(self, genie_id: str) -> AlbumDto | None:
        album: AlbumDocument = AlbumDocument.objects(genie_id=genie_id).first()

        if not album:
            return None

        return album.to_dto()

    def find_all(self) -> list[AlbumDto]:
        albums: list[AlbumDocument] = list(AlbumDocument.objects)
        return [album.to_dto() for album in albums]
