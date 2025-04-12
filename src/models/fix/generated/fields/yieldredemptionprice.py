
from .base import FIXFieldBase
from .types import FIXPrice

class YieldRedemptionPrice(FIXFieldBase):
    """FIX YieldRedemptionPrice field."""
    tag: str = "697"
    name: str = "YieldRedemptionPrice"
    type: str = "PRICE"
    value: FIXPrice
