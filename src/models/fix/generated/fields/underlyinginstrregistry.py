
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingInstrRegistry(FIXFieldBase):
    """FIX UnderlyingInstrRegistry field."""
    tag: str = "595"
    name: str = "UnderlyingInstrRegistry"
    type: str = "STRING"
    value: FIXString
