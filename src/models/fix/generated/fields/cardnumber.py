"""
FIX CardNumber field (tag 489).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CardNumberField(FIXFieldBase):
    """"""
    tag: str = "489"
    name: str = "CardNumber"
    type: str = "STRING"
    value: str
