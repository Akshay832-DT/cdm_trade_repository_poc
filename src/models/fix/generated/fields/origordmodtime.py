"""
FIX OrigOrdModTime field (tag 586).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrigOrdModTimeField(FIXFieldBase):
    """"""
    tag: str = "586"
    name: str = "OrigOrdModTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
