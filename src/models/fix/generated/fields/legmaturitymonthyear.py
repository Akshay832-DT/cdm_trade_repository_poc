
from .base import FIXFieldBase
from .types import FIXMonthYear

class LegMaturityMonthYear(FIXFieldBase):
    """FIX LegMaturityMonthYear field."""
    tag: str = "610"
    name: str = "LegMaturityMonthYear"
    type: str = "MONTHYEAR"
    value: FIXMonthYear
