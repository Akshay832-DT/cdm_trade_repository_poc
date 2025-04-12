
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class YieldCalcDate(FIXFieldBase):
    """FIX YieldCalcDate field."""
    tag: str = "701"
    name: str = "YieldCalcDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
