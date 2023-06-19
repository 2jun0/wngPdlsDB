from wngPdlsDB.document import TagDocument
from wngPdlsDB.exception import NotFoundTagException
from wngPdlsDB.dto import TagDto


class TagRepository:
    def create_tag(self, genie_id: str, title: str) -> TagDto:
        tag = TagDocument(genie_id=genie_id, title=title)
        saved: TagDocument = tag.save()
        return saved.to_dto()

    def delete_by_genie_id(self, genie_id: str) -> None:
        query_set = TagDocument.objects(genie_id=genie_id)

        if not query_set:
            raise NotFoundTagException(f"Can't find tag document: genie_id={genie_id}")

        query_set.delete()

    def find_by_genie_id(self, genie_id: str) -> TagDto | None:
        tag: TagDocument = TagDocument.objects(genie_id=genie_id).first()

        if not tag:
            return None

        return tag.to_dto()

    def find_all(self) -> list[TagDto]:
        tags: list[TagDocument] = list(TagDocument.objects)
        return [tag.to_dto() for tag in tags]
