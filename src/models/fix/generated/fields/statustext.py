"""
FIX StatusText field (tag 929).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StatusTextField(FIXFieldBase):
    """"""
    tag: str = "929"
    name: str = "StatusText"
    type: str = "STRING"
    value: str
