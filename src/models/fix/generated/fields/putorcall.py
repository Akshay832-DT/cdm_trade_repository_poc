
from .base import FIXFieldBase
from .types import FIXInt

class PutOrCall(FIXFieldBase):
    """FIX PutOrCall field."""
    tag: str = "201"
    name: str = "PutOrCall"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: PUT
    # 1: CALL
