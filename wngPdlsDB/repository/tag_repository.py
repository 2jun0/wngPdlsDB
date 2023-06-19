from wngPdlsDB.document import Tag


class TagRepository:
    def create_tag(self, genie_id: str, title: str) -> Tag:
        tag = Tag(genie_id=genie_id, title=title)
        return tag.save()
        
        
    def delete_tag(self, genie_id: str) -> None:
        self.__find(genie_id=genie_id)

