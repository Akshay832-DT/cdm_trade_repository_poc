
from .base import FIXFieldBase
from .types import FIXString

class Symbol(FIXFieldBase):
    """FIX Symbol field."""
    tag: str = "55"
    name: str = "Symbol"
    type: str = "STRING"
    value: FIXString
