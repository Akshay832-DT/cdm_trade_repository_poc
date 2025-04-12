
from .base import FIXFieldBase
from .types import FIXBoolean

class ReportToExch(FIXFieldBase):
    """FIX ReportToExch field."""
    tag: str = "113"
    name: str = "ReportToExch"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
