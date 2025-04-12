
from .base import FIXFieldBase
from .types import FIXInt

class ListSeqNo(FIXFieldBase):
    """FIX ListSeqNo field."""
    tag: str = "67"
    name: str = "ListSeqNo"
    type: str = "INT"
    value: FIXInt
