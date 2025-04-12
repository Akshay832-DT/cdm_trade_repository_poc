
from .base import FIXFieldBase
from .types import FIXString

class PriceImprovement(FIXFieldBase):
    """FIX PriceImprovement field."""
    tag: str = "639"
    name: str = "PriceImprovement"
    type: str = "PRICEOFFSET"
    value: FIXString
