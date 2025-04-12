
from .base import FIXFieldBase
from .types import FIXMonthYear

class UnderlyingMaturityMonthYear(FIXFieldBase):
    """FIX UnderlyingMaturityMonthYear field."""
    tag: str = "313"
    name: str = "UnderlyingMaturityMonthYear"
    type: str = "MONTHYEAR"
    value: FIXMonthYear
