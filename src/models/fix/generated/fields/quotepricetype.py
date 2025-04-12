
from .base import FIXFieldBase
from .types import FIXInt

class QuotePriceType(FIXFieldBase):
    """FIX QuotePriceType field."""
    tag: str = "692"
    name: str = "QuotePriceType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: PERCENT
    # 2: PER_SHARE
    # 3: FIXED_AMOUNT
    # 4: DISCOUNT
    # 5: PREMIUM
    # 6: SPREAD
    # 7: TED_PRICE
    # 8: TED_YIELD
    # 9: YIELD_SPREAD
    # 10: YIELD
