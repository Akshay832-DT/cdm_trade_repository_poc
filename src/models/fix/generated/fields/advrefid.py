"""
FIX AdvRefID field (tag 3).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AdvRefIDField(FIXFieldBase):
    """"""
    tag: str = "3"
    name: str = "AdvRefID"
    type: str = "STRING"
    value: str
