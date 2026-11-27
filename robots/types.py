from dataclasses import dataclass

@dataclass
class Event:
    id: int
    pos: list[float]
    confidence: float
    last_seen: float
    reported_by: int