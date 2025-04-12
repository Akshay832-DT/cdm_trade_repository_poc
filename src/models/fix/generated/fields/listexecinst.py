
from .base import FIXFieldBase
from .types import FIXString

class ListExecInst(FIXFieldBase):
    """FIX ListExecInst field."""
    tag: str = "69"
    name: str = "ListExecInst"
    type: str = "STRING"
    value: FIXString
