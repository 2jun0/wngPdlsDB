from wngPdlsDB.document import Tag


class TagRepository:
    def create_tag(self, genie_id: str, title: str):
        tag = Tag(genie_id=genie_id, title=title)
        tag.save()
