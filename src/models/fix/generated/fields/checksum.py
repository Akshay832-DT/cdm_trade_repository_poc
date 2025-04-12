
from .base import FIXFieldBase
from .types import FIXString

class CheckSum(FIXFieldBase):
    """FIX CheckSum field."""
    tag: str = "10"
    name: str = "CheckSum"
    type: str = "STRING"
    value: FIXString
