"""
FIX ContAmtCurr field (tag 521).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContAmtCurrField(FIXFieldBase):
    """"""
    tag: str = "521"
    name: str = "ContAmtCurr"
    type: str = "CURRENCY"
    value: str
