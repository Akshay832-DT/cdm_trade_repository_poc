"""
FIX SenderCompID field (tag 49).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SenderCompIDField(FIXFieldBase):
    """"""
    tag: str = "49"
    name: str = "SenderCompID"
    type: str = "STRING"
    value: str
