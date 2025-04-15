"""
FIX PosMaintRptID field (tag 721).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosMaintRptIDField(FIXFieldBase):
    """"""
    tag: str = "721"
    name: str = "PosMaintRptID"
    type: str = "STRING"
    value: str
