"""
FIX RefSubID field (tag 931).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RefSubIDField(FIXFieldBase):
    """"""
    tag: str = "931"
    name: str = "RefSubID"
    type: str = "STRING"
    value: str
