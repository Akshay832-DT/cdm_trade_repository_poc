"""
FIX UnderlyingMaturityDate field (tag 542).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingMaturityDateField(FIXFieldBase):
    """"""
    tag: str = "542"
    name: str = "UnderlyingMaturityDate"
    type: str = "LOCALMKTDATE"
    value: date
