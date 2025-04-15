"""
FIX UnderlyingStipType field (tag 888).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingStipTypeField(FIXFieldBase):
    """"""
    tag: str = "888"
    name: str = "UnderlyingStipType"
    type: str = "STRING"
    value: str
