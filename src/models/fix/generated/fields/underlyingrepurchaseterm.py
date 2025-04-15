"""
FIX UnderlyingRepurchaseTerm field (tag 244).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingRepurchaseTermField(FIXFieldBase):
    """"""
    tag: str = "244"
    name: str = "UnderlyingRepurchaseTerm"
    type: str = "INT"
    value: int
