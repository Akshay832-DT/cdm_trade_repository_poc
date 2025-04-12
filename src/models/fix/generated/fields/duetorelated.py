
from .base import FIXFieldBase
from .types import FIXBoolean

class DueToRelated(FIXFieldBase):
    """FIX DueToRelated field."""
    tag: str = "329"
    name: str = "DueToRelated"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
