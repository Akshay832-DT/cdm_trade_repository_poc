
from .base import FIXFieldBase
from .types import FIXBoolean

class GapFillFlag(FIXFieldBase):
    """FIX GapFillFlag field."""
    tag: str = "123"
    name: str = "GapFillFlag"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
