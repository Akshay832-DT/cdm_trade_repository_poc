"""
FIX CardStartDate field (tag 503).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CardStartDateField(FIXFieldBase):
    """"""
    tag: str = "503"
    name: str = "CardStartDate"
    type: str = "LOCALMKTDATE"
    value: date
