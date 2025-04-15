"""
FIX SettlDate field (tag 64).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlDateField(FIXFieldBase):
    """"""
    tag: str = "64"
    name: str = "SettlDate"
    type: str = "LOCALMKTDATE"
    value: date
