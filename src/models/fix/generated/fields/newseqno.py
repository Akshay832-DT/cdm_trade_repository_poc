
from .base import FIXFieldBase
from .types import FIXSeqNum

class NewSeqNo(FIXFieldBase):
    """FIX NewSeqNo field."""
    tag: str = "36"
    name: str = "NewSeqNo"
    type: str = "SEQNUM"
    value: FIXSeqNum
