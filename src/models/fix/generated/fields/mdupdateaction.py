
from .base import FIXFieldBase
from .types import FIXChar

class MDUpdateAction(FIXFieldBase):
    """FIX MDUpdateAction field."""
    tag: str = "279"
    name: str = "MDUpdateAction"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: NEW
    # 1: CHANGE
    # 2: DELETE
