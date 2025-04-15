"""
FIX NewSeqNo field (tag 36).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NewSeqNoField(FIXFieldBase):
    """"""
    tag: str = "36"
    name: str = "NewSeqNo"
    type: str = "SEQNUM"
    value: int
