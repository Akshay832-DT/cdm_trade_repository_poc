"""
FIX TransBkdTime field (tag 483).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TransBkdTimeField(FIXFieldBase):
    """"""
    tag: str = "483"
    name: str = "TransBkdTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
