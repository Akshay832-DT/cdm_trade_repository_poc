"""
FIX TimeBracket field (tag 943).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TimeBracketField(FIXFieldBase):
    """"""
    tag: str = "943"
    name: str = "TimeBracket"
    type: str = "STRING"
    value: str
