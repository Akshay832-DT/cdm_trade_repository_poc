
from .base import FIXFieldBase
from .types import FIXFloat

class SettlCurrOfferFxRate(FIXFieldBase):
    """FIX SettlCurrOfferFxRate field."""
    tag: str = "657"
    name: str = "SettlCurrOfferFxRate"
    type: str = "FLOAT"
    value: FIXFloat
