"""
FIX StrikeTime field (tag 443).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StrikeTimeField(FIXFieldBase):
    """"""
    tag: str = "443"
    name: str = "StrikeTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
