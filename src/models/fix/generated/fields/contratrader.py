"""
FIX ContraTrader field (tag 337).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContraTraderField(FIXFieldBase):
    """"""
    tag: str = "337"
    name: str = "ContraTrader"
    type: str = "STRING"
    value: str
