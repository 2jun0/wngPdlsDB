from wngPdlsDB.document import Tag
from mongoengine import QuerySet


class TagRepository:
    def create_tag(self, genie_id: str, title: str) -> Tag:
        tag = Tag(genie_id=genie_id, title=title)
        return tag.save()

    def delete_tag(self, genie_id: str) -> None:
        self.__find(genie_id=genie_id)

    def find_by_genie_id(self, genie_id: str) -> Tag:
        return Tag.objects(genie_id=genie_id).first()

    def find_all(self) -> QuerySet:
        return Tag.objects
