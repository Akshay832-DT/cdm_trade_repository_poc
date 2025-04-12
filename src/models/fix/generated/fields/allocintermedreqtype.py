
from .base import FIXFieldBase
from .types import FIXInt

class AllocIntermedReqType(FIXFieldBase):
    """FIX AllocIntermedReqType field."""
    tag: str = "808"
    name: str = "AllocIntermedReqType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: PENDING_ACCEPT
    # 2: PENDING_RELEASE
    # 3: PENDING_REVERSAL
    # 4: ACCEPT
    # 5: BLOCK_LEVEL_REJECT
    # 6: ACCOUNT_LEVEL_REJECT
