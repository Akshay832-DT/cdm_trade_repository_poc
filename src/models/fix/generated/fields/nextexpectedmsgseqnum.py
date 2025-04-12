
from .base import FIXFieldBase
from .types import FIXSeqNum

class NextExpectedMsgSeqNum(FIXFieldBase):
    """FIX NextExpectedMsgSeqNum field."""
    tag: str = "789"
    name: str = "NextExpectedMsgSeqNum"
    type: str = "SEQNUM"
    value: FIXSeqNum
