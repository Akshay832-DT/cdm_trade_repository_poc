
from .base import FIXFieldBase
from .types import FIXPercentage

class AccruedInterestRate(FIXFieldBase):
    """FIX AccruedInterestRate field."""
    tag: str = "158"
    name: str = "AccruedInterestRate"
    type: str = "PERCENTAGE"
    value: FIXPercentage
