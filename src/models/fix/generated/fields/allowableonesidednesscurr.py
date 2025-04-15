"""
FIX AllowableOneSidednessCurr field (tag 767).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllowableOneSidednessCurrField(FIXFieldBase):
    """"""
    tag: str = "767"
    name: str = "AllowableOneSidednessCurr"
    type: str = "CURRENCY"
    value: str
