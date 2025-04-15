"""
FIX LastUpdateTime field (tag 779).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastUpdateTimeField(FIXFieldBase):
    """"""
    tag: str = "779"
    name: str = "LastUpdateTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
