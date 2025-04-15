"""
FIX LegIOIQty field (tag 682).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegIOIQtyField(FIXFieldBase):
    """"""
    tag: str = "682"
    name: str = "LegIOIQty"
    type: str = "STRING"
    value: str
