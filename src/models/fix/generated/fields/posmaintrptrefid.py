"""
FIX PosMaintRptRefID field (tag 714).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosMaintRptRefIDField(FIXFieldBase):
    """"""
    tag: str = "714"
    name: str = "PosMaintRptRefID"
    type: str = "STRING"
    value: str
