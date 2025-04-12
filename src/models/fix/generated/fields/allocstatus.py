
from .base import FIXFieldBase
from .types import FIXInt

class AllocStatus(FIXFieldBase):
    """FIX AllocStatus field."""
    tag: str = "87"
    name: str = "AllocStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: ACCEPTED
    # 1: BLOCK_LEVEL_REJECT
    # 2: ACCOUNT_LEVEL_REJECT
    # 3: RECEIVED
    # 4: INCOMPLETE
    # 5: REJECTED_BY_INTERMEDIARY
