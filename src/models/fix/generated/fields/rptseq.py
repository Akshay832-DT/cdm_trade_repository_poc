"""
FIX RptSeq field (tag 83).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RptSeqField(FIXFieldBase):
    """"""
    tag: str = "83"
    name: str = "RptSeq"
    type: str = "INT"
    value: int
