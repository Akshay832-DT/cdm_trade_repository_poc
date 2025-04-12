
from .base import FIXFieldBase
from .types import FIXBoolean

class OddLot(FIXFieldBase):
    """FIX OddLot field."""
    tag: str = "575"
    name: str = "OddLot"
    type: str = "BOOLEAN"
    value: FIXBoolean

    # Enum values
    # Y: YES
    # N: NO
