
from .base import FIXFieldBase
from .types import FIXInt

class TradeRequestStatus(FIXFieldBase):
    """FIX TradeRequestStatus field."""
    tag: str = "750"
    name: str = "TradeRequestStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: ACCEPTED
    # 1: COMPLETED
    # 2: REJECTED
