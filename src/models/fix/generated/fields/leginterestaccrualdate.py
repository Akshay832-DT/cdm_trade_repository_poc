
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class LegInterestAccrualDate(FIXFieldBase):
    """FIX LegInterestAccrualDate field."""
    tag: str = "956"
    name: str = "LegInterestAccrualDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
