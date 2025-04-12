
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class UnderlyingRedemptionDate(FIXFieldBase):
    """FIX UnderlyingRedemptionDate field."""
    tag: str = "247"
    name: str = "UnderlyingRedemptionDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
