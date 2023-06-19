from wngPdlsDB.document import ArtistDocument
from wngPdlsDB.document import ArtistDto


class ArtistRepository:
    def create_artist(self, genie_id: str, name: str) -> ArtistDto:
        artist = ArtistDocument(genie_id=genie_id, name=name)
        saved: ArtistDocument = artist.save()
        return saved.to_dto()

    def delete_artist(self, genie_id: str) -> None:
        self.find_by_genie_id(genie_id).delete()

    def find_by_genie_id(self, genie_id: str) -> ArtistDto:
        artist: ArtistDocument = ArtistDocument.objects(genie_id=genie_id).first()
        return artist.to_dto()

    def find_all(self) -> list[ArtistDto]:
        artists: list[ArtistDocument] = list(ArtistDocument.objects)
        return [artist.to_dto() for artist in artists]
