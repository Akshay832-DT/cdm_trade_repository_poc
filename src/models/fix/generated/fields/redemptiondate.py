
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class RedemptionDate(FIXFieldBase):
    """FIX RedemptionDate field."""
    tag: str = "240"
    name: str = "RedemptionDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
