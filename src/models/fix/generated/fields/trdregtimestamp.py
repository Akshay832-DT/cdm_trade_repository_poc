"""
FIX TrdRegTimestamp field (tag 769).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TrdRegTimestampField(FIXFieldBase):
    """"""
    tag: str = "769"
    name: str = "TrdRegTimestamp"
    type: str = "UTCTIMESTAMP"
    value: datetime
