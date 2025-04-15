"""
FIX LegQty field (tag 687).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegQtyField(FIXFieldBase):
    """"""
    tag: str = "687"
    name: str = "LegQty"
    type: str = "QTY"
    value: float
