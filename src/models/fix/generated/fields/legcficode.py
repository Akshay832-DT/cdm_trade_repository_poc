"""
FIX LegCFICode field (tag 608).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegCFICodeField(FIXFieldBase):
    """"""
    tag: str = "608"
    name: str = "LegCFICode"
    type: str = "STRING"
    value: str
