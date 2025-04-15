"""
FIX ExDate field (tag 230).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExDateField(FIXFieldBase):
    """"""
    tag: str = "230"
    name: str = "ExDate"
    type: str = "LOCALMKTDATE"
    value: date
