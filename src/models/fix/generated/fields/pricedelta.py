
from .base import FIXFieldBase
from .types import FIXFloat

class PriceDelta(FIXFieldBase):
    """FIX PriceDelta field."""
    tag: str = "811"
    name: str = "PriceDelta"
    type: str = "FLOAT"
    value: FIXFloat
