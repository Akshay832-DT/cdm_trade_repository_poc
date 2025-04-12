
from .base import FIXFieldBase
from .types import FIXInt

class LegPriceType(FIXFieldBase):
    """FIX LegPriceType field."""
    tag: str = "686"
    name: str = "LegPriceType"
    type: str = "INT"
    value: FIXInt
