
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class PaymentDate(FIXFieldBase):
    """FIX PaymentDate field."""
    tag: str = "504"
    name: str = "PaymentDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
