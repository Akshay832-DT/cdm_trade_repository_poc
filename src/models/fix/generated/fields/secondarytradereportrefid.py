
from .base import FIXFieldBase
from .types import FIXString

class SecondaryTradeReportRefID(FIXFieldBase):
    """FIX SecondaryTradeReportRefID field."""
    tag: str = "881"
    name: str = "SecondaryTradeReportRefID"
    type: str = "STRING"
    value: FIXString
