"""
FIX TargetSubID field (tag 57).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TargetSubIDField(FIXFieldBase):
    """"""
    tag: str = "57"
    name: str = "TargetSubID"
    type: str = "STRING"
    value: str
