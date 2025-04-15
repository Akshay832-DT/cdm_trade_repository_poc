"""
FIX LegRefID field (tag 654).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegRefIDField(FIXFieldBase):
    """"""
    tag: str = "654"
    name: str = "LegRefID"
    type: str = "STRING"
    value: str
