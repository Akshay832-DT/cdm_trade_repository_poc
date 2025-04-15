"""
FIX CrossID field (tag 548).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CrossIDField(FIXFieldBase):
    """"""
    tag: str = "548"
    name: str = "CrossID"
    type: str = "STRING"
    value: str
