"""
FIX ContraLegRefID field (tag 655).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContraLegRefIDField(FIXFieldBase):
    """"""
    tag: str = "655"
    name: str = "ContraLegRefID"
    type: str = "STRING"
    value: str
