
from .base import FIXFieldBase
from .types import FIXInt

class TrdSubType(FIXFieldBase):
    """FIX TrdSubType field."""
    tag: str = "829"
    name: str = "TrdSubType"
    type: str = "INT"
    value: FIXInt
