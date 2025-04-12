
from .base import FIXFieldBase
from .types import FIXCurrency

class LegStrikeCurrency(FIXFieldBase):
    """FIX LegStrikeCurrency field."""
    tag: str = "942"
    name: str = "LegStrikeCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
