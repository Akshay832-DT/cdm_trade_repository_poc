
from .base import FIXFieldBase
from .types import FIXInt

class YieldRedemptionPriceType(FIXFieldBase):
    """FIX YieldRedemptionPriceType field."""
    tag: str = "698"
    name: str = "YieldRedemptionPriceType"
    type: str = "INT"
    value: FIXInt
