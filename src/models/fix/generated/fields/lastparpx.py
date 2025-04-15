"""
FIX LastParPx field (tag 669).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastParPxField(FIXFieldBase):
    """"""
    tag: str = "669"
    name: str = "LastParPx"
    type: str = "PRICE"
    value: float
