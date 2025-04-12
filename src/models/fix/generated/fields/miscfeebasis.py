
from .base import FIXFieldBase
from .types import FIXInt

class MiscFeeBasis(FIXFieldBase):
    """FIX MiscFeeBasis field."""
    tag: str = "891"
    name: str = "MiscFeeBasis"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: ABSOLUTE
    # 1: PER_UNIT
    # 2: PERCENTAGE
