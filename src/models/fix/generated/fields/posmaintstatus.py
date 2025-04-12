
from .base import FIXFieldBase
from .types import FIXInt

class PosMaintStatus(FIXFieldBase):
    """FIX PosMaintStatus field."""
    tag: str = "722"
    name: str = "PosMaintStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: ACCEPTED
    # 1: ACCEPTED_WITH_WARNINGS
    # 2: REJECTED
    # 3: COMPLETED
    # 4: COMPLETED_WITH_WARNINGS
