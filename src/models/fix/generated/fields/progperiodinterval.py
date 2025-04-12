
from .base import FIXFieldBase
from .types import FIXInt

class ProgPeriodInterval(FIXFieldBase):
    """FIX ProgPeriodInterval field."""
    tag: str = "415"
    name: str = "ProgPeriodInterval"
    type: str = "INT"
    value: FIXInt
