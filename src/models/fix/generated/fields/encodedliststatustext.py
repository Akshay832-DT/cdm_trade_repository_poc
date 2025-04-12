
from .base import FIXFieldBase
from .types import FIXData

class EncodedListStatusText(FIXFieldBase):
    """FIX EncodedListStatusText field."""
    tag: str = "446"
    name: str = "EncodedListStatusText"
    type: str = "DATA"
    value: FIXData
