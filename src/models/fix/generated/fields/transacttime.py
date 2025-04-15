"""
FIX TransactTime field (tag 60).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TransactTimeField(FIXFieldBase):
    """"""
    tag: str = "60"
    name: str = "TransactTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
