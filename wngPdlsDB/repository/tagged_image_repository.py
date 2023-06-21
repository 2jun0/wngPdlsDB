from wngPdlsDB.document import TaggedImageDocument
from wngPdlsDB.dto import TaggedImageDto, TagDto
from wngPdlsDB.exception import NotFoundImageException
from wngPdlsDB.repository.common import _find_tag_docs_by_dto, _find_tag_doc_by_dto


class TaggedImageRepository:
    def create_image(
        self,
        url: str,
        tags: list[TagDto],
    ) -> TaggedImageDocument:
        image = TaggedImageDocument(
            url=url,
            tags=_find_tag_docs_by_dto(tags),
        )
        saved: TaggedImageDocument = image.save()
        return saved.to_dto()

    def delete_by_id(self, id: str) -> None:
        query_set = TaggedImageDocument.objects(id=id)

        if not query_set:
            raise NotFoundImageException(f"Can't find image document: id={id}")

        query_set.delete()

    def find_by_id(self, id: str) -> TaggedImageDto | None:
        image: TaggedImageDocument = TaggedImageDocument.objects(id=id).first()

        if not image:
            return None

        return image.to_dto()

    def find_all(self) -> list[TaggedImageDto]:
        images: list[TaggedImageDocument] = list(TaggedImageDocument.objects)
        return [image.to_dto() for image in images]

    def find_by_tag(self, tag: TagDto) -> list[TaggedImageDto]:
        tag_doc = _find_tag_doc_by_dto(tag)
        images: list[TaggedImageDocument] = list(
            TaggedImageDocument.objects(tags=tag_doc)
        )
        return [image.to_dto() for image in images]
