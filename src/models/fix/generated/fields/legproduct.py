"""
FIX LegProduct field (tag 607).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegProductField(FIXFieldBase):
    """"""
    tag: str = "607"
    name: str = "LegProduct"
    type: str = "INT"
    value: int
