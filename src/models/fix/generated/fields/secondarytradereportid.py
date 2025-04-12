
from .base import FIXFieldBase
from .types import FIXString

class SecondaryTradeReportID(FIXFieldBase):
    """FIX SecondaryTradeReportID field."""
    tag: str = "818"
    name: str = "SecondaryTradeReportID"
    type: str = "STRING"
    value: FIXString
