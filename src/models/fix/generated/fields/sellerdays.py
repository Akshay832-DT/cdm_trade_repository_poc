"""
FIX SellerDays field (tag 287).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SellerDaysField(FIXFieldBase):
    """"""
    tag: str = "287"
    name: str = "SellerDays"
    type: str = "INT"
    value: int
