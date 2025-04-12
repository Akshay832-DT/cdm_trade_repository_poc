
from .base import FIXFieldBase
from .types import FIXPercentage

class CouponRate(FIXFieldBase):
    """FIX CouponRate field."""
    tag: str = "223"
    name: str = "CouponRate"
    type: str = "PERCENTAGE"
    value: FIXPercentage
