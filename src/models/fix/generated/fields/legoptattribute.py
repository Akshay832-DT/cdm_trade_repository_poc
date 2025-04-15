"""
FIX LegOptAttribute field (tag 613).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegOptAttributeField(FIXFieldBase):
    """"""
    tag: str = "613"
    name: str = "LegOptAttribute"
    type: str = "CHAR"
    value: str
