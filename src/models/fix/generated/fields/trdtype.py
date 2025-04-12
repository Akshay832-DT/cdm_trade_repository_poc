
from .base import FIXFieldBase
from .types import FIXInt

class TrdType(FIXFieldBase):
    """FIX TrdType field."""
    tag: str = "828"
    name: str = "TrdType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: REGULAR_TRADE
    # 1: BLOCK_TRADE
    # 2: EFP
    # 3: TRANSFER
    # 4: LATE_TRADE
    # 5: T_TRADE
    # 6: WEIGHTED_AVERAGE_PRICE_TRADE
    # 7: BUNCHED_TRADE
    # 8: LATE_BUNCHED_TRADE
    # 9: PRIOR_REFERENCE_PRICE_TRADE
    # 10: AFTER_HOURS_TRADE
