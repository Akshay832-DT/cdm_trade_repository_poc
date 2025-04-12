
from .base import FIXFieldBase
from .types import FIXBoolean

class ResetSeqNumFlag(FIXFieldBase):
    """FIX ResetSeqNumFlag field."""
    tag: str = "141"
    name: str = "ResetSeqNumFlag"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
