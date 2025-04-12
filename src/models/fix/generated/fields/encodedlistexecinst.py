
from .base import FIXFieldBase
from .types import FIXData

class EncodedListExecInst(FIXFieldBase):
    """FIX EncodedListExecInst field."""
    tag: str = "353"
    name: str = "EncodedListExecInst"
    type: str = "DATA"
    value: FIXData
