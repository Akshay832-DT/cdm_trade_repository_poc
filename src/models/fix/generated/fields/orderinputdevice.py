
from .base import FIXFieldBase
from .types import FIXString

class OrderInputDevice(FIXFieldBase):
    """FIX OrderInputDevice field."""
    tag: str = "821"
    name: str = "OrderInputDevice"
    type: str = "STRING"
    value: FIXString
