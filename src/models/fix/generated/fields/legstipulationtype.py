"""
FIX LegStipulationType field (tag 688).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegStipulationTypeField(FIXFieldBase):
    """"""
    tag: str = "688"
    name: str = "LegStipulationType"
    type: str = "STRING"
    value: str
