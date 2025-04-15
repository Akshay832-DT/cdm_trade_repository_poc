"""
FIX LastMsgSeqNumProcessed field (tag 369).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastMsgSeqNumProcessedField(FIXFieldBase):
    """"""
    tag: str = "369"
    name: str = "LastMsgSeqNumProcessed"
    type: str = "SEQNUM"
    value: int
