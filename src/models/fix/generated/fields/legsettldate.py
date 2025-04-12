
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class LegSettlDate(FIXFieldBase):
    """FIX LegSettlDate field."""
    tag: str = "588"
    name: str = "LegSettlDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
