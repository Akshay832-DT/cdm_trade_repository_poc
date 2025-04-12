
from .base import FIXFieldBase
from .types import FIXPrice

class AllocPrice(FIXFieldBase):
    """FIX AllocPrice field."""
    tag: str = "366"
    name: str = "AllocPrice"
    type: str = "PRICE"
    value: FIXPrice
