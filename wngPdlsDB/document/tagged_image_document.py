from mongoengine import Document, URLField, ReferenceField, ListField, ValidationError
from wngPdlsDB.dto import TaggedImageDto
from wngPdlsDB.document.tag_document import TagDocument


def should_have_at_least_one_tag(tags: list[TagDocument]):
    if len(tags) <= 0:
        raise ValidationError(f"TaggedImage should have at least one tags")


class TaggedImageDocument(Document):
    url = URLField(required=True)
    tags = ListField(
        ReferenceField(TagDocument),
        required=True,
        validation=should_have_at_least_one_tag,
    )

    def to_dto(self) -> TaggedImageDto:
        return TaggedImageDto(
            str(self.id), self.url, [tag.to_dto() for tag in self.tags]
        )
