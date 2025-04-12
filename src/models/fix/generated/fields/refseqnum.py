
from .base import FIXFieldBase
from .types import FIXSeqNum

class RefSeqNum(FIXFieldBase):
    """FIX RefSeqNum field."""
    tag: str = "45"
    name: str = "RefSeqNum"
    type: str = "SEQNUM"
    value: FIXSeqNum
