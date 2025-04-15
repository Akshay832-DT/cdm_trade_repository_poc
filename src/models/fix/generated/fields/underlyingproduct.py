"""
FIX UnderlyingProduct field (tag 462).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingProductField(FIXFieldBase):
    """"""
    tag: str = "462"
    name: str = "UnderlyingProduct"
    type: str = "INT"
    value: int
