"""
FIX LegDatedDate field (tag 739).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegDatedDateField(FIXFieldBase):
    """"""
    tag: str = "739"
    name: str = "LegDatedDate"
    type: str = "LOCALMKTDATE"
    value: date
