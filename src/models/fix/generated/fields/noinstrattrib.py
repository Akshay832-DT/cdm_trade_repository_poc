"""
FIX NoInstrAttrib field (tag 870).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoInstrAttribField(FIXFieldBase):
    """"""
    tag: str = "870"
    name: str = "NoInstrAttrib"
    type: str = "NUMINGROUP"
    value: int
