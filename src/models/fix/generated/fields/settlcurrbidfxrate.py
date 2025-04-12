
from .base import FIXFieldBase
from .types import FIXFloat

class SettlCurrBidFxRate(FIXFieldBase):
    """FIX SettlCurrBidFxRate field."""
    tag: str = "656"
    name: str = "SettlCurrBidFxRate"
    type: str = "FLOAT"
    value: FIXFloat
