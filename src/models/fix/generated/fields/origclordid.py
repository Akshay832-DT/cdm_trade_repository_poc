"""
FIX OrigClOrdID field (tag 41).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrigClOrdIDField(FIXFieldBase):
    """"""
    tag: str = "41"
    name: str = "OrigClOrdID"
    type: str = "STRING"
    value: str
