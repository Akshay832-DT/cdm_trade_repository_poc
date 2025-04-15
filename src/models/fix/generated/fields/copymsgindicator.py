"""
FIX CopyMsgIndicator field (tag 797).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CopyMsgIndicatorField(FIXFieldBase):
    """"""
    tag: str = "797"
    name: str = "CopyMsgIndicator"
    type: str = "BOOLEAN"
    value: bool
