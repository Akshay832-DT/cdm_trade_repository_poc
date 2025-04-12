
from .base import FIXFieldBase
from .types import FIXSeqNum

class BeginSeqNo(FIXFieldBase):
    """FIX BeginSeqNo field."""
    tag: str = "7"
    name: str = "BeginSeqNo"
    type: str = "SEQNUM"
    value: FIXSeqNum
