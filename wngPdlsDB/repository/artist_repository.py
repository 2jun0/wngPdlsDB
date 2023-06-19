from wngPdlsDB.document import ArtistDocument
from wngPdlsDB.exception import NotFoundArtistException
from wngPdlsDB.dto import ArtistDto


class ArtistRepository:
    def create_artist(self, genie_id: str, name: str) -> ArtistDto:
        artist = ArtistDocument(genie_id=genie_id, name=name)
        saved: ArtistDocument = artist.save()
        return saved.to_dto()

    def delete_by_genie_id(self, genie_id: str) -> None:
        artist: ArtistDocument = ArtistDocument.objects(genie_id=genie_id)

        if not artist:
            raise NotFoundArtistException(
                f"Can't find artist document: genie_id={genie_id}"
            )

        artist.delete()

    def find_by_genie_id(self, genie_id: str) -> ArtistDto:
        artist: ArtistDocument = ArtistDocument.objects(genie_id=genie_id).first()

        if not artist:
            return None

        return artist.to_dto()

    def find_all(self) -> list[ArtistDto]:
        artists: list[ArtistDocument] = list(ArtistDocument.objects)
        return [artist.to_dto() for artist in artists]
