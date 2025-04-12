
from .base import FIXFieldBase
from .types import FIXString

class LegCFICode(FIXFieldBase):
    """FIX LegCFICode field."""
    tag: str = "608"
    name: str = "LegCFICode"
    type: str = "STRING"
    value: FIXString
