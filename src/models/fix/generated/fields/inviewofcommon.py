
from .base import FIXFieldBase
from .types import FIXBoolean

class InViewOfCommon(FIXFieldBase):
    """FIX InViewOfCommon field."""
    tag: str = "328"
    name: str = "InViewOfCommon"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
