"""
FIX LegStipulationValue field (tag 689).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegStipulationValueField(FIXFieldBase):
    """"""
    tag: str = "689"
    name: str = "LegStipulationValue"
    type: str = "STRING"
    value: str
