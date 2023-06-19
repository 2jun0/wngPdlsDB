from dataclasses import dataclass
from wngPdlsDB.dto.tag_dto import TagDto


@dataclass
class ImageDto:
    id: str
    url: str
    tag: TagDto
