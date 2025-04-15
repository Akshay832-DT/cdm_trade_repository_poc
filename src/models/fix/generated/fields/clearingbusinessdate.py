"""
FIX ClearingBusinessDate field (tag 715).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ClearingBusinessDateField(FIXFieldBase):
    """"""
    tag: str = "715"
    name: str = "ClearingBusinessDate"
    type: str = "LOCALMKTDATE"
    value: date
