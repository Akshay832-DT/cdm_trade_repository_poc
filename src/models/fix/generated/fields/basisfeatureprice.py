"""
FIX BasisFeaturePrice field (tag 260).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BasisFeaturePriceField(FIXFieldBase):
    """"""
    tag: str = "260"
    name: str = "BasisFeaturePrice"
    type: str = "PRICE"
    value: float
