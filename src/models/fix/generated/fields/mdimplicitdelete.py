
from .base import FIXFieldBase
from .types import FIXBoolean

class MDImplicitDelete(FIXFieldBase):
    """FIX MDImplicitDelete field."""
    tag: str = "547"
    name: str = "MDImplicitDelete"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
