
from .base import FIXFieldBase
from .types import FIXBoolean

class ExchangeForPhysical(FIXFieldBase):
    """FIX ExchangeForPhysical field."""
    tag: str = "411"
    name: str = "ExchangeForPhysical"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
