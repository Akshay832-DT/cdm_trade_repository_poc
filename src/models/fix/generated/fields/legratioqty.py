
from .base import FIXFieldBase
from .types import FIXFloat

class LegRatioQty(FIXFieldBase):
    """FIX LegRatioQty field."""
    tag: str = "623"
    name: str = "LegRatioQty"
    type: str = "FLOAT"
    value: FIXFloat
