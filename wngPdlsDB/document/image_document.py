from mongoengine import (
    Document,
    URLField,
    ReferenceField,
)
from wngPdlsDB.dto import ImageDto
from wngPdlsDB.document.tag_document import TagDocument


class ImageDocument(Document):
    url = URLField(required=True)
    tag = ReferenceField(TagDocument, required=True)

    def to_dto(self) -> ImageDto:
        return ImageDto(
            str(self.id),
            self.url,
            self.tag.to_dto(),
        )