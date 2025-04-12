
from .base import FIXFieldBase
from .types import FIXChar

class BasisPxType(FIXFieldBase):
    """FIX BasisPxType field."""
    tag: str = "419"
    name: str = "BasisPxType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 2: CLOSING_PRICE_AT_MORNING_SESSION
    # 3: CLOSING_PRICE
    # 4: CURRENT_PRICE
    # 5: SQ
    # 6: VWAP_THROUGH_A_DAY
    # 7: VWAP_THROUGH_A_MORNING_SESSION
    # 8: VWAP_THROUGH_AN_AFTERNOON_SESSION
    # 9: VWAP_THROUGH_A_DAY_EXCEPT
    # A: VWAP_THROUGH_A_MORNING_SESSION_EXCEPT
    # B: VWAP_THROUGH_AN_AFTERNOON_SESSION_EXCEPT
    # C: STRIKE
    # D: OPEN
    # Z: OTHERS
