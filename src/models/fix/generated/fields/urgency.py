
from .base import FIXFieldBase
from .types import FIXChar

class Urgency(FIXFieldBase):
    """FIX Urgency field."""
    tag: str = "61"
    name: str = "Urgency"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: NORMAL
    # 1: FLASH
    # 2: BACKGROUND
