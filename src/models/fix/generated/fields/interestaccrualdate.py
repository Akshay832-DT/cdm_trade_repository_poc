"""
FIX InterestAccrualDate field (tag 874).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class InterestAccrualDateField(FIXFieldBase):
    """"""
    tag: str = "874"
    name: str = "InterestAccrualDate"
    type: str = "LOCALMKTDATE"
    value: date
