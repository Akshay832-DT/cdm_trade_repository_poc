
from .base import FIXFieldBase
from .types import FIXInt

class UnderlyingSettlPriceType(FIXFieldBase):
    """FIX UnderlyingSettlPriceType field."""
    tag: str = "733"
    name: str = "UnderlyingSettlPriceType"
    type: str = "INT"
    value: FIXInt
