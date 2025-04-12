
from .base import FIXFieldBase
from .types import FIXSeqNum

class HopRefID(FIXFieldBase):
    """FIX HopRefID field."""
    tag: str = "630"
    name: str = "HopRefID"
    type: str = "SEQNUM"
    value: FIXSeqNum
