from wngPdlsDB.document import UntaggedImageDocument
from wngPdlsDB.dto import UntaggedImageDto
from wngPdlsDB.exception import NotFoundTagException, NotFoundImageException


class UntaggedImageRepository:
    def create_image(
        self,
        url: str,
    ) -> UntaggedImageDocument:
        image = UntaggedImageDocument(
            url=url,
        )
        saved: UntaggedImageDocument = image.save()
        return saved.to_dto()

    def delete_by_id(self, id: str) -> None:
        query_set = UntaggedImageDocument.objects(id=id)

        if not query_set:
            raise NotFoundImageException(f"Can't find image document: id={id}")

        query_set.delete()

    def find_by_id(self, id: str) -> UntaggedImageDto | None:
        image: UntaggedImageDocument = UntaggedImageDocument.objects(id=id).first()

        if not image:
            return None

        return image.to_dto()

    def find_all(self) -> list[UntaggedImageDto]:
        images: list[UntaggedImageDocument] = list(UntaggedImageDocument.objects)
        return [image.to_dto() for image in images]
