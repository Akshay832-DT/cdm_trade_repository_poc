
from .base import FIXFieldBase
from .types import FIXMonthYear

class MaturityMonthYear(FIXFieldBase):
    """FIX MaturityMonthYear field."""
    tag: str = "200"
    name: str = "MaturityMonthYear"
    type: str = "MONTHYEAR"
    value: FIXMonthYear
