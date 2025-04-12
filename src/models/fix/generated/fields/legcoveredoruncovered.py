
from .base import FIXFieldBase
from .types import FIXInt

class LegCoveredOrUncovered(FIXFieldBase):
    """FIX LegCoveredOrUncovered field."""
    tag: str = "565"
    name: str = "LegCoveredOrUncovered"
    type: str = "INT"
    value: FIXInt
