
from .base import FIXFieldBase
from .types import FIXChar

class PositionEffect(FIXFieldBase):
    """FIX PositionEffect field."""
    tag: str = "77"
    name: str = "PositionEffect"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # O: OPEN
    # C: CLOSE
    # R: ROLLED
    # F: FIFO
