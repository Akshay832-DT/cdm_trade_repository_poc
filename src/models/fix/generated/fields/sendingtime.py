"""
FIX SendingTime field (tag 52).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SendingTimeField(FIXFieldBase):
    """"""
    tag: str = "52"
    name: str = "SendingTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
