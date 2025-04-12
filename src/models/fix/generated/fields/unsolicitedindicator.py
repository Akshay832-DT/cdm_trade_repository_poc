
from .base import FIXFieldBase
from .types import FIXBoolean

class UnsolicitedIndicator(FIXFieldBase):
    """FIX UnsolicitedIndicator field."""
    tag: str = "325"
    name: str = "UnsolicitedIndicator"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
