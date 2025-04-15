"""
FIX MsgSeqNum field (tag 34).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MsgSeqNumField(FIXFieldBase):
    """"""
    tag: str = "34"
    name: str = "MsgSeqNum"
    type: str = "SEQNUM"
    value: int
