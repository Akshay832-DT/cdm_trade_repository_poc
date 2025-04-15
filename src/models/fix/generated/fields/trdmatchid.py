"""
FIX TrdMatchID field (tag 880).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TrdMatchIDField(FIXFieldBase):
    """"""
    tag: str = "880"
    name: str = "TrdMatchID"
    type: str = "STRING"
    value: str
