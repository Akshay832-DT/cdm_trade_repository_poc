
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingSymbol(FIXFieldBase):
    """FIX UnderlyingSymbol field."""
    tag: str = "311"
    name: str = "UnderlyingSymbol"
    type: str = "STRING"
    value: FIXString
