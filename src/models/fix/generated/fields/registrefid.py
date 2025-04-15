"""
FIX RegistRefID field (tag 508).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RegistRefIDField(FIXFieldBase):
    """"""
    tag: str = "508"
    name: str = "RegistRefID"
    type: str = "STRING"
    value: str
