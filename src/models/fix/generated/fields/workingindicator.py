
from .base import FIXFieldBase
from .types import FIXBoolean

class WorkingIndicator(FIXFieldBase):
    """FIX WorkingIndicator field."""
    tag: str = "636"
    name: str = "WorkingIndicator"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
