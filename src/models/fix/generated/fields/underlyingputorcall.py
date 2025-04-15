"""
FIX UnderlyingPutOrCall field (tag 315).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingPutOrCallField(FIXFieldBase):
    """"""
    tag: str = "315"
    name: str = "UnderlyingPutOrCall"
    type: str = "INT"
    value: int
