
from .base import FIXFieldBase
from .types import FIXString

class LegSymbol(FIXFieldBase):
    """FIX LegSymbol field."""
    tag: str = "600"
    name: str = "LegSymbol"
    type: str = "STRING"
    value: FIXString
