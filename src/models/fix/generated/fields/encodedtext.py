
from .base import FIXFieldBase
from .types import FIXData

class EncodedText(FIXFieldBase):
    """FIX EncodedText field."""
    tag: str = "355"
    name: str = "EncodedText"
    type: str = "DATA"
    value: FIXData
