
from .base import FIXFieldBase
from .types import FIXInt

class AllocHandlInst(FIXFieldBase):
    """FIX AllocHandlInst field."""
    tag: str = "209"
    name: str = "AllocHandlInst"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: MATCH
    # 2: FORWARD
    # 3: FORWARD_AND_MATCH
