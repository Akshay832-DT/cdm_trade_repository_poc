"""
FIX LegMaturityDate field (tag 611).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegMaturityDateField(FIXFieldBase):
    """"""
    tag: str = "611"
    name: str = "LegMaturityDate"
    type: str = "LOCALMKTDATE"
    value: date
