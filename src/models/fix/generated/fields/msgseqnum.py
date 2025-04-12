
from .base import FIXFieldBase
from .types import FIXSeqNum

class MsgSeqNum(FIXFieldBase):
    """FIX MsgSeqNum field."""
    tag: str = "34"
    name: str = "MsgSeqNum"
    type: str = "SEQNUM"
    value: FIXSeqNum
