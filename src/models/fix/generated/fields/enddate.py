
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class EndDate(FIXFieldBase):
    """FIX EndDate field."""
    tag: str = "917"
    name: str = "EndDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
