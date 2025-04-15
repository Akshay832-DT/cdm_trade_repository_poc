"""
FIX Price2 field (tag 640).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Price2Field(FIXFieldBase):
    """"""
    tag: str = "640"
    name: str = "Price2"
    type: str = "PRICE"
    value: float
