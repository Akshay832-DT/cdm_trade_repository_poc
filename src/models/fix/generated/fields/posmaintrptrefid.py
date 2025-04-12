
from .base import FIXFieldBase
from .types import FIXString

class PosMaintRptRefID(FIXFieldBase):
    """FIX PosMaintRptRefID field."""
    tag: str = "714"
    name: str = "PosMaintRptRefID"
    type: str = "STRING"
    value: FIXString
