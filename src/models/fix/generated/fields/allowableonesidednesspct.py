
from .base import FIXFieldBase
from .types import FIXPercentage

class AllowableOneSidednessPct(FIXFieldBase):
    """FIX AllowableOneSidednessPct field."""
    tag: str = "765"
    name: str = "AllowableOneSidednessPct"
    type: str = "PERCENTAGE"
    value: FIXPercentage
