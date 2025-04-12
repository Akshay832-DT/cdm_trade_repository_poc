
from .base import FIXFieldBase
from .types import FIXBoolean

class PossResend(FIXFieldBase):
    """FIX PossResend field."""
    tag: str = "97"
    name: str = "PossResend"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
