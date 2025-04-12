
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class InterestAccrualDate(FIXFieldBase):
    """FIX InterestAccrualDate field."""
    tag: str = "874"
    name: str = "InterestAccrualDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
