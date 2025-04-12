
from .base import FIXFieldBase
from .types import FIXString

class LegInstrRegistry(FIXFieldBase):
    """FIX LegInstrRegistry field."""
    tag: str = "599"
    name: str = "LegInstrRegistry"
    type: str = "STRING"
    value: FIXString
