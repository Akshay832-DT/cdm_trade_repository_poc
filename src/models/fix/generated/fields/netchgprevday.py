"""
FIX NetChgPrevDay field (tag 451).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NetChgPrevDayField(FIXFieldBase):
    """"""
    tag: str = "451"
    name: str = "NetChgPrevDay"
    type: str = "PRICEOFFSET"
    value: float
