
from .base import FIXFieldBase
from .types import FIXPercentage

class UnderlyingCouponRate(FIXFieldBase):
    """FIX UnderlyingCouponRate field."""
    tag: str = "435"
    name: str = "UnderlyingCouponRate"
    type: str = "PERCENTAGE"
    value: FIXPercentage
