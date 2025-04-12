
from .base import FIXFieldBase
from .types import FIXInt

class ListOrderStatus(FIXFieldBase):
    """FIX ListOrderStatus field."""
    tag: str = "431"
    name: str = "ListOrderStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: IN_BIDDING_PROCESS
    # 2: RECEIVED_FOR_EXECUTION
    # 3: EXECUTING
    # 4: CANCELLING
    # 5: ALERT
    # 6: ALL_DONE
    # 7: REJECT
