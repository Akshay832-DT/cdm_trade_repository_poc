
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class UnderlyingCouponPaymentDate(FIXFieldBase):
    """FIX UnderlyingCouponPaymentDate field."""
    tag: str = "241"
    name: str = "UnderlyingCouponPaymentDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
