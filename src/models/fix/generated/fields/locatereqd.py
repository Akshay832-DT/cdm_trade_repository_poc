
from .base import FIXFieldBase
from .types import FIXBoolean

class LocateReqd(FIXFieldBase):
    """FIX LocateReqd field."""
    tag: str = "114"
    name: str = "LocateReqd"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
