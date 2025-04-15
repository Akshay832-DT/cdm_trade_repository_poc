"""
FIX StipulationValue field (tag 234).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StipulationValueField(FIXFieldBase):
    """"""
    tag: str = "234"
    name: str = "StipulationValue"
    type: str = "STRING"
    value: str
