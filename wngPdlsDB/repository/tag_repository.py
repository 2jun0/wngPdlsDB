from wngPdlsDB.document import TagDocument
from wngPdlsDB.dto.tag_dto import TagDto


class TagRepository:
    def create_tag(self, genie_id: str, title: str) -> TagDto:
        tag = TagDocument(genie_id=genie_id, title=title)
        saved: TagDocument = tag.save()
        return saved.to_dto()

    def delete_tag(self, genie_id: str) -> None:
        self.find_by_genie_id(genie_id).delete()

    def find_by_genie_id(self, genie_id: str) -> TagDto:
        tag: TagDocument = TagDocument.objects(genie_id=genie_id).first()
        return tag.to_dto()

    def find_all(self) -> list[TagDto]:
        tags: list[TagDocument] = list(TagDocument.objects)
        return [tag.to_dto() for tag in tags]
