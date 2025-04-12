
from .base import FIXFieldBase
from .types import FIXString

class AllocReportID(FIXFieldBase):
    """FIX AllocReportID field."""
    tag: str = "755"
    name: str = "AllocReportID"
    type: str = "STRING"
    value: FIXString
