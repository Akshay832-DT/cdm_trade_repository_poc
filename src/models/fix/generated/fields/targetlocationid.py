
from .base import FIXFieldBase
from .types import FIXString

class TargetLocationID(FIXFieldBase):
    """FIX TargetLocationID field."""
    tag: str = "143"
    name: str = "TargetLocationID"
    type: str = "STRING"
    value: FIXString
