"""
FIX NextExpectedMsgSeqNum field (tag 789).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NextExpectedMsgSeqNumField(FIXFieldBase):
    """"""
    tag: str = "789"
    name: str = "NextExpectedMsgSeqNum"
    type: str = "SEQNUM"
    value: int
