"""
FIX SettlDate2 field (tag 193).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlDate2Field(FIXFieldBase):
    """"""
    tag: str = "193"
    name: str = "SettlDate2"
    type: str = "LOCALMKTDATE"
    value: date
