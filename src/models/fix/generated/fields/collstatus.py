
from .base import FIXFieldBase
from .types import FIXInt

class CollStatus(FIXFieldBase):
    """FIX CollStatus field."""
    tag: str = "910"
    name: str = "CollStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: UNASSIGNED
    # 1: PARTIALLY_ASSIGNED
    # 2: ASSIGNMENT_PROPOSED
    # 3: ASSIGNED
    # 4: CHALLENGED
