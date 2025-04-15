"""
FIX NoDistribInsts field (tag 510).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoDistribInstsField(FIXFieldBase):
    """"""
    tag: str = "510"
    name: str = "NoDistribInsts"
    type: str = "NUMINGROUP"
    value: int
