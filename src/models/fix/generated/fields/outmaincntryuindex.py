"""
FIX OutMainCntryUIndex field (tag 412).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OutMainCntryUIndexField(FIXFieldBase):
    """"""
    tag: str = "412"
    name: str = "OutMainCntryUIndex"
    type: str = "AMT"
    value: float
