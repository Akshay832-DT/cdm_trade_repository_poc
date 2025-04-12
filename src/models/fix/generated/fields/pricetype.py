
from .base import FIXFieldBase
from .types import FIXInt

class PriceType(FIXFieldBase):
    """FIX PriceType field."""
    tag: str = "423"
    name: str = "PriceType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: PERCENTAGE
    # 2: PER_UNIT
    # 3: FIXED_AMOUNT
    # 4: DISCOUNT
    # 5: PREMIUM
    # 6: SPREAD
    # 7: TED_PRICE
    # 8: TED_YIELD
    # 9: YIELD
    # 10: FIXED_CABINET_TRADE_PRICE
    # 11: VARIABLE_CABINET_TRADE_PRICE
