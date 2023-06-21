from mongoengine import Document, URLField, ReferenceField, ListField
from wngPdlsDB.dto import TaggedImageDto
from wngPdlsDB.document.tag_document import TagDocument


class TaggedImageDocument(Document):
    url = URLField(required=True)
    tags = ListField(ReferenceField(TagDocument), required=True)

    def to_dto(self) -> TaggedImageDto:
        return TaggedImageDto(
            str(self.id), self.url, [tag.to_dto() for tag in self.tags]
        )
