
from .base import FIXFieldBase
from .types import FIXBoolean

class SolicitedFlag(FIXFieldBase):
    """FIX SolicitedFlag field."""
    tag: str = "377"
    name: str = "SolicitedFlag"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
