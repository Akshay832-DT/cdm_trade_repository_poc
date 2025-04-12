
from .base import FIXFieldBase
from .types import FIXPercentage

class LegCouponRate(FIXFieldBase):
    """FIX LegCouponRate field."""
    tag: str = "615"
    name: str = "LegCouponRate"
    type: str = "PERCENTAGE"
    value: FIXPercentage
