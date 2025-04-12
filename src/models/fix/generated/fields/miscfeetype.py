
from .base import FIXFieldBase
from .types import FIXChar

class MiscFeeType(FIXFieldBase):
    """FIX MiscFeeType field."""
    tag: str = "139"
    name: str = "MiscFeeType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: REGULATORY
    # 2: TAX
    # 3: LOCAL_COMMISSION
    # 4: EXCHANGE_FEES
    # 5: STAMP
    # 6: LEVY
    # 7: OTHER
    # 8: MARKUP
    # 9: CONSUMPTION_TAX
    # 10: PER_TRANSACTION
    # 11: CONVERSION
    # 12: AGENT
