
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class ClearingBusinessDate(FIXFieldBase):
    """FIX ClearingBusinessDate field."""
    tag: str = "715"
    name: str = "ClearingBusinessDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
