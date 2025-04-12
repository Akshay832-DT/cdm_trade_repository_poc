
from .base import FIXFieldBase
from .types import FIXBoolean

class IOINaturalFlag(FIXFieldBase):
    """FIX IOINaturalFlag field."""
    tag: str = "130"
    name: str = "IOINaturalFlag"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
