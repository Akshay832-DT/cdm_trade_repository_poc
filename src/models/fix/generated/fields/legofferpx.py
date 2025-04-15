"""
FIX LegOfferPx field (tag 684).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegOfferPxField(FIXFieldBase):
    """"""
    tag: str = "684"
    name: str = "LegOfferPx"
    type: str = "PRICE"
    value: float
