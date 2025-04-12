
from .base import FIXFieldBase
from .types import FIXInt

class ProgRptReqs(FIXFieldBase):
    """FIX ProgRptReqs field."""
    tag: str = "414"
    name: str = "ProgRptReqs"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: BUY_SIDE_REQUESTS
    # 2: SELL_SIDE_SENDS
    # 3: REAL_TIME_EXECUTION_REPORTS
