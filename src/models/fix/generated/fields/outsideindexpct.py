
from .base import FIXFieldBase
from .types import FIXPercentage

class OutsideIndexPct(FIXFieldBase):
    """FIX OutsideIndexPct field."""
    tag: str = "407"
    name: str = "OutsideIndexPct"
    type: str = "PERCENTAGE"
    value: FIXPercentage
