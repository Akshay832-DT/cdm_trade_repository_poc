"""
FIX SecurityID field (tag 48).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityIDField(FIXFieldBase):
    """"""
    tag: str = "48"
    name: str = "SecurityID"
    type: str = "STRING"
    value: str
