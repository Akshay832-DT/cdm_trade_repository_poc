
from .base import FIXFieldBase
from .types import FIXInt

class AllocCancReplaceReason(FIXFieldBase):
    """FIX AllocCancReplaceReason field."""
    tag: str = "796"
    name: str = "AllocCancReplaceReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: ORIGINAL_DETAILS_INCOMPLETE
    # 2: CHANGE_IN_UNDERLYING_ORDER_DETAILS
    # 99: OTHER
