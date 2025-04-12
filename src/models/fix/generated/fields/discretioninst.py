
from .base import FIXFieldBase
from .types import FIXChar

class DiscretionInst(FIXFieldBase):
    """FIX DiscretionInst field."""
    tag: str = "388"
    name: str = "DiscretionInst"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: RELATED_TO_DISPLAYED_PRICE
    # 1: RELATED_TO_MARKET_PRICE
    # 2: RELATED_TO_PRIMARY_PRICE
    # 3: RELATED_TO_LOCAL_PRIMARY_PRICE
    # 4: RELATED_TO_MIDPOINT_PRICE
    # 5: RELATED_TO_LAST_TRADE_PRICE
    # 6: RELATED_TO_VWAP
