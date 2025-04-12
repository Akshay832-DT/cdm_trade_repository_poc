
from .base import FIXFieldBase
from .types import FIXPrice

class LegLastPx(FIXFieldBase):
    """FIX LegLastPx field."""
    tag: str = "637"
    name: str = "LegLastPx"
    type: str = "PRICE"
    value: FIXPrice
