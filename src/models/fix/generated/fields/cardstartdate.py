
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class CardStartDate(FIXFieldBase):
    """FIX CardStartDate field."""
    tag: str = "503"
    name: str = "CardStartDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
