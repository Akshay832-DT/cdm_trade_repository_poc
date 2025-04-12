
from .base import FIXFieldBase
from .types import FIXBoolean

class LastFragment(FIXFieldBase):
    """FIX LastFragment field."""
    tag: str = "893"
    name: str = "LastFragment"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
