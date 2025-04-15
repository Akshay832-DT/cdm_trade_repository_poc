"""
FIX LegAllocAcctIDSource field (tag 674).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegAllocAcctIDSourceField(FIXFieldBase):
    """"""
    tag: str = "674"
    name: str = "LegAllocAcctIDSource"
    type: str = "STRING"
    value: str
