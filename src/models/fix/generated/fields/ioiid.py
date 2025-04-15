"""
FIX IOIID field (tag 23).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IOIIDField(FIXFieldBase):
    """"""
    tag: str = "23"
    name: str = "IOIID"
    type: str = "STRING"
    value: str
