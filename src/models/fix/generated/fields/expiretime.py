"""
FIX ExpireTime field (tag 126).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExpireTimeField(FIXFieldBase):
    """"""
    tag: str = "126"
    name: str = "ExpireTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
