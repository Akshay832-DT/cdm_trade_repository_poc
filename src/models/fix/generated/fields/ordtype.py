
from .base import FIXFieldBase
from .types import FIXChar

class OrdType(FIXFieldBase):
    """FIX OrdType field."""
    tag: str = "40"
    name: str = "OrdType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: MARKET
    # 2: LIMIT
    # 3: STOP
    # 4: STOP_LIMIT
    # 6: WITH_OR_WITHOUT
    # 7: LIMIT_OR_BETTER
    # 8: LIMIT_WITH_OR_WITHOUT
    # 9: ON_BASIS
    # D: PREVIOUSLY_QUOTED
    # E: PREVIOUSLY_INDICATED
    # G: FOREX_SWAP
    # I: FUNARI
    # J: MARKET_IF_TOUCHED
    # K: MARKET_WITH_LEFT_OVER_AS_LIMIT
    # L: PREVIOUS_FUND_VALUATION_POINT
    # M: NEXT_FUND_VALUATION_POINT
    # P: PEGGED
