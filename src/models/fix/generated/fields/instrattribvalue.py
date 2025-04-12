
from .base import FIXFieldBase
from .types import FIXString

class InstrAttribValue(FIXFieldBase):
    """FIX InstrAttribValue field."""
    tag: str = "872"
    name: str = "InstrAttribValue"
    type: str = "STRING"
    value: FIXString
