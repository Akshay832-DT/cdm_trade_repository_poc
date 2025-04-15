"""
FIX SecondaryExecID field (tag 527).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecondaryExecIDField(FIXFieldBase):
    """"""
    tag: str = "527"
    name: str = "SecondaryExecID"
    type: str = "STRING"
    value: str
