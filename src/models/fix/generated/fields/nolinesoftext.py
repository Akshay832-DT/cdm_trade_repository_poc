"""
FIX NoLinesOfText field (tag 33).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoLinesOfTextField(FIXFieldBase):
    """"""
    tag: str = "33"
    name: str = "NoLinesOfText"
    type: str = "NUMINGROUP"
    value: int
