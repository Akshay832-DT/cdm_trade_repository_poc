
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class TradeDate(FIXFieldBase):
    """FIX TradeDate field."""
    tag: str = "75"
    name: str = "TradeDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
