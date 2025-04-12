
from .base import FIXFieldBase
from .types import FIXInt

class PosMaintAction(FIXFieldBase):
    """FIX PosMaintAction field."""
    tag: str = "712"
    name: str = "PosMaintAction"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: NEW
    # 2: REPLACE
    # 3: CANCEL
