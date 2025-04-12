
from .base import FIXFieldBase
from .types import FIXInt

class RefTagID(FIXFieldBase):
    """FIX RefTagID field."""
    tag: str = "371"
    name: str = "RefTagID"
    type: str = "INT"
    value: FIXInt
