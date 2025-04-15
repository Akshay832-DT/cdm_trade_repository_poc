"""
FIX MktOfferPx field (tag 646).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MktOfferPxField(FIXFieldBase):
    """"""
    tag: str = "646"
    name: str = "MktOfferPx"
    type: str = "PRICE"
    value: float
