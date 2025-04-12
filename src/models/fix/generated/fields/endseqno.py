
from .base import FIXFieldBase
from .types import FIXSeqNum

class EndSeqNo(FIXFieldBase):
    """FIX EndSeqNo field."""
    tag: str = "16"
    name: str = "EndSeqNo"
    type: str = "SEQNUM"
    value: FIXSeqNum
