
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class TradeOriginationDate(FIXFieldBase):
    """FIX TradeOriginationDate field."""
    tag: str = "229"
    name: str = "TradeOriginationDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
