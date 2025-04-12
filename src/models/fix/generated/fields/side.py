
from .base import FIXFieldBase
from .types import FIXChar

class Side(FIXFieldBase):
    """FIX Side field."""
    tag: str = "54"
    name: str = "Side"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: BUY
    # 2: SELL
    # 3: BUY_MINUS
    # 4: SELL_PLUS
    # 5: SELL_SHORT
    # 6: SELL_SHORT_EXEMPT
    # 7: UNDISCLOSED
    # 8: CROSS
    # 9: CROSS_SHORT
    # A: CROSS_SHORT_EXEMPT
    # B: AS_DEFINED
    # C: OPPOSITE
    # D: SUBSCRIBE
    # E: REDEEM
    # F: LEND
    # G: BORROW
