
from .base import FIXFieldBase
from .types import FIXBoolean

class LastRptRequested(FIXFieldBase):
    """FIX LastRptRequested field."""
    tag: str = "912"
    name: str = "LastRptRequested"
    type: str = "BOOLEAN"
    value: FIXBoolean
