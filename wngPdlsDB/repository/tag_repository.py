from wngPdlsDB.document import TagDocument
from mongoengine import QuerySet


class TagRepository:
        tag = TagDocument(genie_id=genie_id, title=title)

    def delete_tag(self, genie_id: str) -> None:
        self.find_by_genie_id(genie_id).delete()

    def find_by_genie_id(self, genie_id: str) -> Tag:
        return TagDocument.objects(genie_id=genie_id).first()

    def find_all(self) -> QuerySet:
        return TagDocument.objects
