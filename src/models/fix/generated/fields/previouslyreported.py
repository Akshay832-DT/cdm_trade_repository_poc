
from .base import FIXFieldBase
from .types import FIXBoolean

class PreviouslyReported(FIXFieldBase):
    """FIX PreviouslyReported field."""
    tag: str = "570"
    name: str = "PreviouslyReported"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
