"""
FIX ClOrdID field (tag 11).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ClOrdIDField(FIXFieldBase):
    """"""
    tag: str = "11"
    name: str = "ClOrdID"
    type: str = "STRING"
    value: str
