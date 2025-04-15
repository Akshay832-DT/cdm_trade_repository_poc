"""
FIX OrigTime field (tag 42).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrigTimeField(FIXFieldBase):
    """"""
    tag: str = "42"
    name: str = "OrigTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
