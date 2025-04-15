"""
FIX UnderlyingOptAttribute field (tag 317).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingOptAttributeField(FIXFieldBase):
    """"""
    tag: str = "317"
    name: str = "UnderlyingOptAttribute"
    type: str = "CHAR"
    value: str
