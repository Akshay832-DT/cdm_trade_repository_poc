
from .base import FIXFieldBase
from .types import FIXPrice

class PrevClosePx(FIXFieldBase):
    """FIX PrevClosePx field."""
    tag: str = "140"
    name: str = "PrevClosePx"
    type: str = "PRICE"
    value: FIXPrice
