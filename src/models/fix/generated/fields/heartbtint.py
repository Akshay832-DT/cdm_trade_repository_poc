"""
FIX HeartBtInt field (tag 108).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class HeartBtIntField(FIXFieldBase):
    """"""
    tag: str = "108"
    name: str = "HeartBtInt"
    type: str = "INT"
    value: int
