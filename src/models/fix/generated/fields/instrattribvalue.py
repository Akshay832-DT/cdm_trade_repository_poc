"""
FIX InstrAttribValue field (tag 872).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class InstrAttribValueField(FIXFieldBase):
    """"""
    tag: str = "872"
    name: str = "InstrAttribValue"
    type: str = "STRING"
    value: str
