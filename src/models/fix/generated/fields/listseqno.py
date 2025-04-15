"""
FIX ListSeqNo field (tag 67).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ListSeqNoField(FIXFieldBase):
    """"""
    tag: str = "67"
    name: str = "ListSeqNo"
    type: str = "INT"
    value: int
