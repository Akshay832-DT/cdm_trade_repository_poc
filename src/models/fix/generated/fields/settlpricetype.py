
from .base import FIXFieldBase
from .types import FIXInt

class SettlPriceType(FIXFieldBase):
    """FIX SettlPriceType field."""
    tag: str = "731"
    name: str = "SettlPriceType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: FINAL
    # 2: THEORETICAL
