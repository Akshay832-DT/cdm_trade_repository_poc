"""
FIX EndSeqNo field (tag 16).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EndSeqNoField(FIXFieldBase):
    """"""
    tag: str = "16"
    name: str = "EndSeqNo"
    type: str = "SEQNUM"
    value: int
