"""
FIX MDEntryBuyer field (tag 288).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntryBuyerField(FIXFieldBase):
    """"""
    tag: str = "288"
    name: str = "MDEntryBuyer"
    type: str = "STRING"
    value: str
