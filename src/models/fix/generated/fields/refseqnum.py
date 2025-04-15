"""
FIX RefSeqNum field (tag 45).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RefSeqNumField(FIXFieldBase):
    """"""
    tag: str = "45"
    name: str = "RefSeqNum"
    type: str = "SEQNUM"
    value: int
