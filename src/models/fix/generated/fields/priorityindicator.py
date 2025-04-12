
from .base import FIXFieldBase
from .types import FIXInt

class PriorityIndicator(FIXFieldBase):
    """FIX PriorityIndicator field."""
    tag: str = "638"
    name: str = "PriorityIndicator"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: PRIORITY_UNCHANGED
    # 1: LOST_PRIORITY_AS_RESULT_OF_ORDER_CHANGE
