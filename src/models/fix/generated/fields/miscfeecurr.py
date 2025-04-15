"""
FIX MiscFeeCurr field (tag 138).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MiscFeeCurrField(FIXFieldBase):
    """"""
    tag: str = "138"
    name: str = "MiscFeeCurr"
    type: str = "CURRENCY"
    value: str
