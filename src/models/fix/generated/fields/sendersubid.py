"""
FIX SenderSubID field (tag 50).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SenderSubIDField(FIXFieldBase):
    """"""
    tag: str = "50"
    name: str = "SenderSubID"
    type: str = "STRING"
    value: str
