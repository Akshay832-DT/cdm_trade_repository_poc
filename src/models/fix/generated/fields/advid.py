"""
FIX AdvId field (tag 2).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AdvIdField(FIXFieldBase):
    """"""
    tag: str = "2"
    name: str = "AdvId"
    type: str = "STRING"
    value: str
