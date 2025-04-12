
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class CardExpDate(FIXFieldBase):
    """FIX CardExpDate field."""
    tag: str = "490"
    name: str = "CardExpDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
