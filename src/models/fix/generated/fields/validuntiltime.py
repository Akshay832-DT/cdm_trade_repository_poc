"""
FIX ValidUntilTime field (tag 62).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ValidUntilTimeField(FIXFieldBase):
    """"""
    tag: str = "62"
    name: str = "ValidUntilTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
