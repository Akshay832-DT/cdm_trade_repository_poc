"""
FIX UnderlyingCFICode field (tag 463).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingCFICodeField(FIXFieldBase):
    """"""
    tag: str = "463"
    name: str = "UnderlyingCFICode"
    type: str = "STRING"
    value: str
