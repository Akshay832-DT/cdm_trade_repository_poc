
from .base import FIXFieldBase
from .types import FIXString

class PosMaintRptID(FIXFieldBase):
    """FIX PosMaintRptID field."""
    tag: str = "721"
    name: str = "PosMaintRptID"
    type: str = "STRING"
    value: FIXString
