
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingSymbolSfx(FIXFieldBase):
    """FIX UnderlyingSymbolSfx field."""
    tag: str = "312"
    name: str = "UnderlyingSymbolSfx"
    type: str = "STRING"
    value: FIXString
