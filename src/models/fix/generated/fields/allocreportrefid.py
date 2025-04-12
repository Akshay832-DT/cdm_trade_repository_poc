
from .base import FIXFieldBase
from .types import FIXString

class AllocReportRefID(FIXFieldBase):
    """FIX AllocReportRefID field."""
    tag: str = "795"
    name: str = "AllocReportRefID"
    type: str = "STRING"
    value: FIXString
