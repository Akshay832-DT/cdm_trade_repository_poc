"""
FIX OfferSize field (tag 135).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OfferSizeField(FIXFieldBase):
    """"""
    tag: str = "135"
    name: str = "OfferSize"
    type: str = "QTY"
    value: float
