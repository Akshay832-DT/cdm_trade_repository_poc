"""
FIX StartDate field (tag 916).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StartDateField(FIXFieldBase):
    """"""
    tag: str = "916"
    name: str = "StartDate"
    type: str = "LOCALMKTDATE"
    value: date
