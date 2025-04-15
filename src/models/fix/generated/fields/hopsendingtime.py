"""
FIX HopSendingTime field (tag 629).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class HopSendingTimeField(FIXFieldBase):
    """"""
    tag: str = "629"
    name: str = "HopSendingTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
