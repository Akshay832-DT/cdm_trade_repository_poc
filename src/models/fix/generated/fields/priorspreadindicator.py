"""
FIX PriorSpreadIndicator field (tag 720).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PriorSpreadIndicatorField(FIXFieldBase):
    """"""
    tag: str = "720"
    name: str = "PriorSpreadIndicator"
    type: str = "BOOLEAN"
    value: bool
