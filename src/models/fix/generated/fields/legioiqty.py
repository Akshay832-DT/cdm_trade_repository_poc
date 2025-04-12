
from .base import FIXFieldBase
from .types import FIXString

class LegIOIQty(FIXFieldBase):
    """FIX LegIOIQty field."""
    tag: str = "682"
    name: str = "LegIOIQty"
    type: str = "STRING"
    value: FIXString
