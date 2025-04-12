
from .base import FIXFieldBase
from .types import FIXData

class RawData(FIXFieldBase):
    """FIX RawData field."""
    tag: str = "96"
    name: str = "RawData"
    type: str = "DATA"
    value: FIXData
