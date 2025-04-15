"""
FIX AllocAcctIDSource field (tag 661).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocAcctIDSourceField(FIXFieldBase):
    """"""
    tag: str = "661"
    name: str = "AllocAcctIDSource"
    type: str = "INT"
    value: int
