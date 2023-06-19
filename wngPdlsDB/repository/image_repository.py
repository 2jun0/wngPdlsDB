from wngPdlsDB.document import ImageDocument, TagDocument
from wngPdlsDB.dto import ImageDto, TagDto


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
        self.find_by_id(id).delete()

    def find_by_id(self, id: str) -> ImageDto:
        image: ImageDocument = ImageDocument.objects(id=id)
        return image.to_dto()

    def find_all(self) -> list[ImageDto]:
        images: list[ImageDocument] = list(ImageDocument.objects)
        return [image.to_dto() for image in images]

    def find_by_tag(self, tag: TagDto) -> list[ImageDto]:
        tag_doc = self.__find_tag_doc_by_dto(tag)
        images: list[ImageDocument] = list(ImageDocument.objects(tag=tag_doc))
        return [image.to_dto() for image in images]

    def __find_tag_doc_by_dto(self, tag: TagDto) -> TagDocument:
        return TagDocument.objects(genie_id=tag.genie_id).first()
