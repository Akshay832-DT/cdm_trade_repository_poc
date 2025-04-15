"""
FIX NoContraBrokers field (tag 382).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoContraBrokersField(FIXFieldBase):
    """"""
    tag: str = "382"
    name: str = "NoContraBrokers"
    type: str = "NUMINGROUP"
    value: int
