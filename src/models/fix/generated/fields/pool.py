
from .base import FIXFieldBase
from .types import FIXString

class Pool(FIXFieldBase):
    """FIX Pool field."""
    tag: str = "691"
    name: str = "Pool"
    type: str = "STRING"
    value: FIXString
