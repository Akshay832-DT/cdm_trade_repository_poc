
from .base import FIXFieldBase
from .types import FIXString

class LegSymbolSfx(FIXFieldBase):
    """FIX LegSymbolSfx field."""
    tag: str = "601"
    name: str = "LegSymbolSfx"
    type: str = "STRING"
    value: FIXString
