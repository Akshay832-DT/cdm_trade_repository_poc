"""
FIX Concession field (tag 238).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ConcessionField(FIXFieldBase):
    """"""
    tag: str = "238"
    name: str = "Concession"
    type: str = "AMT"
    value: float
