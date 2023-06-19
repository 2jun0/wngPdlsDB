from dataclasses import dataclass


@dataclass
class TagDto:
    id: str
    genie_id: str
    title: str
