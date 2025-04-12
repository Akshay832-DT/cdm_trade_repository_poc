
from .base import FIXFieldBase
from .types import FIXChar

class IOIQualifier(FIXFieldBase):
    """FIX IOIQualifier field."""
    tag: str = "104"
    name: str = "IOIQualifier"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # A: ALL_OR_NONE
    # B: MARKET_ON_CLOSE
    # C: AT_THE_CLOSE
    # D: VWAP
    # I: IN_TOUCH_WITH
    # L: LIMIT
    # M: MORE_BEHIND
    # O: AT_THE_OPEN
    # P: TAKING_A_POSITION
    # Q: AT_THE_MARKET
    # R: READY_TO_TRADE
    # S: PORTFOLIO_SHOWN
    # T: THROUGH_THE_DAY
    # V: VERSUS
    # W: INDICATION
    # X: CROSSING_OPPORTUNITY
    # Y: AT_THE_MIDPOINT
    # Z: PRE_OPEN
