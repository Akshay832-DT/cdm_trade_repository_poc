"""
FIX OptAttribute field (tag 206).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OptAttributeField(FIXFieldBase):
    """"""
    tag: str = "206"
    name: str = "OptAttribute"
    type: str = "CHAR"
    value: str
