"""
FIX SecondaryTradeReportRefID field (tag 881).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecondaryTradeReportRefIDField(FIXFieldBase):
    """"""
    tag: str = "881"
    name: str = "SecondaryTradeReportRefID"
    type: str = "STRING"
    value: str
