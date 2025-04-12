
from .base import FIXFieldBase
from .types import FIXString

class Spread(FIXFieldBase):
    """FIX Spread field."""
    tag: str = "218"
    name: str = "Spread"
    type: str = "PRICEOFFSET"
    value: FIXString
