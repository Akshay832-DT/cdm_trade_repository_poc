"""
FIX MinOfferSize field (tag 648).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MinOfferSizeField(FIXFieldBase):
    """"""
    tag: str = "648"
    name: str = "MinOfferSize"
    type: str = "QTY"
    value: float
