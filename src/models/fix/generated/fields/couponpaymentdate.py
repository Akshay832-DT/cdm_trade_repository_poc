
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class CouponPaymentDate(FIXFieldBase):
    """FIX CouponPaymentDate field."""
    tag: str = "224"
    name: str = "CouponPaymentDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
