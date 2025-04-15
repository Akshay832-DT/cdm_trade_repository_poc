"""
FIX EndDate field (tag 917).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EndDateField(FIXFieldBase):
    """"""
    tag: str = "917"
    name: str = "EndDate"
    type: str = "LOCALMKTDATE"
    value: date
