"""
FIX RegistEmail field (tag 511).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RegistEmailField(FIXFieldBase):
    """"""
    tag: str = "511"
    name: str = "RegistEmail"
    type: str = "STRING"
    value: str
