"""
FIX MDEntryPx field (tag 270).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntryPxField(FIXFieldBase):
    """"""
    tag: str = "270"
    name: str = "MDEntryPx"
    type: str = "PRICE"
    value: float
