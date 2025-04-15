"""
FIX NoStrikes field (tag 428).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoStrikesField(FIXFieldBase):
    """"""
    tag: str = "428"
    name: str = "NoStrikes"
    type: str = "NUMINGROUP"
    value: int
