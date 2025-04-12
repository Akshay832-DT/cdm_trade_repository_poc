
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class LegRedemptionDate(FIXFieldBase):
    """FIX LegRedemptionDate field."""
    tag: str = "254"
    name: str = "LegRedemptionDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
