from mongoengine import (
    Document,
    URLField,
    ReferenceField,
)
from wngPdlsDB.dto import TaggedImageDto
from wngPdlsDB.document.tag_document import TagDocument


class TaggedImageDocument(Document):
    url = URLField(required=True)
    tag = ReferenceField(TagDocument, required=True)

    def to_dto(self) -> TaggedImageDto:
        return TaggedImageDto(
            str(self.id),
            self.url,
            self.tag.to_dto(),
        )
