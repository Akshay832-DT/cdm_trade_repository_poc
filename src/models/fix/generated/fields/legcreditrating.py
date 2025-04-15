"""
FIX LegCreditRating field (tag 257).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegCreditRatingField(FIXFieldBase):
    """"""
    tag: str = "257"
    name: str = "LegCreditRating"
    type: str = "STRING"
    value: str
