
from .base import FIXFieldBase
from .types import FIXInt

class TradeRequestType(FIXFieldBase):
    """FIX TradeRequestType field."""
    tag: str = "569"
    name: str = "TradeRequestType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: ALL_TRADES
    # 1: MATCHED_TRADES_MATCHING_CRITERIA
    # 2: UNMATCHED_TRADES_THAT_MATCH_CRITERIA
    # 3: UNREPORTED_TRADES_THAT_MATCH_CRITERIA
    # 4: ADVISORIES_THAT_MATCH_CRITERIA
