"""
FIX CreditRating field (tag 255).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CreditRatingField(FIXFieldBase):
    """"""
    tag: str = "255"
    name: str = "CreditRating"
    type: str = "STRING"
    value: str
