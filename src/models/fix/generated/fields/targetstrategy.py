
from .base import FIXFieldBase
from .types import FIXInt

class TargetStrategy(FIXFieldBase):
    """FIX TargetStrategy field."""
    tag: str = "847"
    name: str = "TargetStrategy"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: VWAP
    # 2: PARTICIPATE
    # 3: MININIZE_MARKET_IMPACT
