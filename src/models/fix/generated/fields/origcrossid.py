"""
FIX OrigCrossID field (tag 551).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrigCrossIDField(FIXFieldBase):
    """"""
    tag: str = "551"
    name: str = "OrigCrossID"
    type: str = "STRING"
    value: str
