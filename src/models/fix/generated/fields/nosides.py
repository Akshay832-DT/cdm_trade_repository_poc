
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoSides(FIXFieldBase):
    """FIX NoSides field."""
    tag: str = "552"
    name: str = "NoSides"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup

    # Enum values
    # 1: ONE_SIDE
    # 2: BOTH_SIDES
