
from .base import FIXFieldBase
from .types import FIXBoolean

class PossDupFlag(FIXFieldBase):
    """FIX PossDupFlag field."""
    tag: str = "43"
    name: str = "PossDupFlag"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
