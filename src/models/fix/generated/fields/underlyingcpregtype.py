"""
FIX UnderlyingCPRegType field (tag 878).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingCPRegTypeField(FIXFieldBase):
    """"""
    tag: str = "878"
    name: str = "UnderlyingCPRegType"
    type: str = "STRING"
    value: str
