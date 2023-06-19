from wngPdlsDB.document import ImageDocument, TagDocument
from wngPdlsDB.dto import ImageDto, TagDto
from wngPdlsDB.exception import NotFoundTagException


class ImageRepository:
    def create_image(
        self,
        url: str,
        tag: TagDto,
    ) -> ImageDocument:
        image = ImageDocument(
            url=url,
            tag=self.__find_tag_doc_by_dto(tag),
        )
        saved: ImageDocument = image.save()
        return saved.to_dto()

    def delete_by_id(self, id: str) -> None:
        ImageDocument.objects(id=id).delete()

    def find_by_id(self, id: str) -> ImageDto | None:
        image: ImageDocument = ImageDocument.objects(id=id).first()

        if not image:
            return None

        return image.to_dto()

    def find_all(self) -> list[ImageDto]:
        images: list[ImageDocument] = list(ImageDocument.objects)
        return [image.to_dto() for image in images]

    def find_by_tag(self, tag: TagDto) -> list[ImageDto]:
        tag_doc = self.__find_tag_doc_by_dto(tag)
        images: list[ImageDocument] = list(ImageDocument.objects(tag=tag_doc))
        return [image.to_dto() for image in images]

    def __find_tag_doc_by_dto(self, tag: TagDto) -> TagDocument:
        query_set = TagDocument.objects(genie_id=tag.genie_id)

        if not query_set:
            raise NotFoundTagException(f"Can't find tag document: {tag}")

        return query_set.first()
