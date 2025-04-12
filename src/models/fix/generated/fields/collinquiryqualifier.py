
from .base import FIXFieldBase
from .types import FIXInt

class CollInquiryQualifier(FIXFieldBase):
    """FIX CollInquiryQualifier field."""
    tag: str = "896"
    name: str = "CollInquiryQualifier"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: TRADE_DATE
    # 1: GC_INSTRUMENT
    # 2: COLLATERAL_INSTRUMENT
    # 3: SUBSTITUTION_ELIGIBLE
    # 4: NOT_ASSIGNED
    # 5: PARTIALLY_ASSIGNED
    # 6: FULLY_ASSIGNED
    # 7: OUTSTANDING_TRADES
