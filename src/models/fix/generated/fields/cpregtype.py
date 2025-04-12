
from .base import FIXFieldBase
from .types import FIXString

class CPRegType(FIXFieldBase):
    """FIX CPRegType field."""
    tag: str = "876"
    name: str = "CPRegType"
    type: str = "STRING"
    value: FIXString
