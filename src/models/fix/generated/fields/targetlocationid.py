"""
FIX TargetLocationID field (tag 143).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TargetLocationIDField(FIXFieldBase):
    """"""
    tag: str = "143"
    name: str = "TargetLocationID"
    type: str = "STRING"
    value: str
