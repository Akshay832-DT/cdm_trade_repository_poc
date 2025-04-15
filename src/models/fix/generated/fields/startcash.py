"""
FIX StartCash field (tag 921).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StartCashField(FIXFieldBase):
    """"""
    tag: str = "921"
    name: str = "StartCash"
    type: str = "AMT"
    value: float
