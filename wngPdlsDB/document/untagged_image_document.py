from mongoengine import (
    Document,
    URLField,
)
from wngPdlsDB.dto import UntaggedImageDto


class UntaggedImageDocument(Document):
    url = URLField(required=True)

    def to_dto(self) -> UntaggedImageDto:
        return UntaggedImageDto(
            str(self.id),
            self.url,
        )
