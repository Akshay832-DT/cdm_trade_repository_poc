
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class YieldRedemptionDate(FIXFieldBase):
    """FIX YieldRedemptionDate field."""
    tag: str = "696"
    name: str = "YieldRedemptionDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
