"""
FIX AllocText field (tag 161).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocTextField(FIXFieldBase):
    """"""
    tag: str = "161"
    name: str = "AllocText"
    type: str = "STRING"
    value: str
