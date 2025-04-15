"""
FIX UnderlyingCreditRating field (tag 256).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingCreditRatingField(FIXFieldBase):
    """"""
    tag: str = "256"
    name: str = "UnderlyingCreditRating"
    type: str = "STRING"
    value: str
