"""
FIX DefOfferSize field (tag 294).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DefOfferSizeField(FIXFieldBase):
    """"""
    tag: str = "294"
    name: str = "DefOfferSize"
    type: str = "QTY"
    value: float
