
from .base import FIXFieldBase
from .types import FIXString

class SymbolSfx(FIXFieldBase):
    """FIX SymbolSfx field."""
    tag: str = "65"
    name: str = "SymbolSfx"
    type: str = "STRING"
    value: FIXString
