
from .base import FIXFieldBase
from .types import FIXString

class InstrRegistry(FIXFieldBase):
    """FIX InstrRegistry field."""
    tag: str = "543"
    name: str = "InstrRegistry"
    type: str = "STRING"
    value: FIXString
