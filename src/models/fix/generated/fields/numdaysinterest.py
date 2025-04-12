
from .base import FIXFieldBase
from .types import FIXInt

class NumDaysInterest(FIXFieldBase):
    """FIX NumDaysInterest field."""
    tag: str = "157"
    name: str = "NumDaysInterest"
    type: str = "INT"
    value: FIXInt
