"""
FIX BeginSeqNo field (tag 7).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BeginSeqNoField(FIXFieldBase):
    """"""
    tag: str = "7"
    name: str = "BeginSeqNo"
    type: str = "SEQNUM"
    value: int
