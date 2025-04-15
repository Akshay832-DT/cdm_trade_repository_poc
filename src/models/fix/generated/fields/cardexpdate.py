"""
FIX CardExpDate field (tag 490).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CardExpDateField(FIXFieldBase):
    """"""
    tag: str = "490"
    name: str = "CardExpDate"
    type: str = "LOCALMKTDATE"
    value: date
