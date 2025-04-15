"""
FIX MaxMessageSize field (tag 383).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MaxMessageSizeField(FIXFieldBase):
    """"""
    tag: str = "383"
    name: str = "MaxMessageSize"
    type: str = "LENGTH"
    value: int
