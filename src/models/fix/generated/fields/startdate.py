
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class StartDate(FIXFieldBase):
    """FIX StartDate field."""
    tag: str = "916"
    name: str = "StartDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
