
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class LegCouponPaymentDate(FIXFieldBase):
    """FIX LegCouponPaymentDate field."""
    tag: str = "248"
    name: str = "LegCouponPaymentDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
