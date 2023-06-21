from dataclasses import dataclass
from wngPdlsDB.dto.tag_dto import TagDto


@dataclass
class TaggedImageDto:
    id: str
    url: str
    tag: TagDto
