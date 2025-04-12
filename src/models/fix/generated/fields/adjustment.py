
from .base import FIXFieldBase
from .types import FIXInt

class Adjustment(FIXFieldBase):
    """FIX Adjustment field."""
    tag: str = "334"
    name: str = "Adjustment"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: CANCEL
    # 2: ERROR
    # 3: CORRECTION
