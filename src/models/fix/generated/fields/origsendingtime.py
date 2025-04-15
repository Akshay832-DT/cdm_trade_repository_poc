"""
FIX OrigSendingTime field (tag 122).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrigSendingTimeField(FIXFieldBase):
    """"""
    tag: str = "122"
    name: str = "OrigSendingTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
