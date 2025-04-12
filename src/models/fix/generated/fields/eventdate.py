
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class EventDate(FIXFieldBase):
    """FIX EventDate field."""
    tag: str = "866"
    name: str = "EventDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
