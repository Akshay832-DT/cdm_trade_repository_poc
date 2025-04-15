"""
FIX AllowableOneSidednessPct field (tag 765).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllowableOneSidednessPctField(FIXFieldBase):
    """"""
    tag: str = "765"
    name: str = "AllowableOneSidednessPct"
    type: str = "PERCENTAGE"
    value: float
