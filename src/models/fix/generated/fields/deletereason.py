
from .base import FIXFieldBase
from .types import FIXChar

class DeleteReason(FIXFieldBase):
    """FIX DeleteReason field."""
    tag: str = "285"
    name: str = "DeleteReason"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: CANCELLATION
    # 1: ERROR
