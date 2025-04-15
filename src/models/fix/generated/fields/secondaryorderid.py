"""
FIX SecondaryOrderID field (tag 198).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecondaryOrderIDField(FIXFieldBase):
    """"""
    tag: str = "198"
    name: str = "SecondaryOrderID"
    type: str = "STRING"
    value: str
