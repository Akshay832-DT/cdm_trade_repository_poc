
from .base import FIXFieldBase
from .types import FIXSeqNum

class LastMsgSeqNumProcessed(FIXFieldBase):
    """FIX LastMsgSeqNumProcessed field."""
    tag: str = "369"
    name: str = "LastMsgSeqNumProcessed"
    type: str = "SEQNUM"
    value: FIXSeqNum
