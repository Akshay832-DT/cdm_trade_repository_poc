"""
FIX LegRepurchaseTerm field (tag 251).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegRepurchaseTermField(FIXFieldBase):
    """"""
    tag: str = "251"
    name: str = "LegRepurchaseTerm"
    type: str = "INT"
    value: int
