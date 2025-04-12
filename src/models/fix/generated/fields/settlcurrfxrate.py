
from .base import FIXFieldBase
from .types import FIXFloat

class SettlCurrFxRate(FIXFieldBase):
    """FIX SettlCurrFxRate field."""
    tag: str = "155"
    name: str = "SettlCurrFxRate"
    type: str = "FLOAT"
    value: FIXFloat
