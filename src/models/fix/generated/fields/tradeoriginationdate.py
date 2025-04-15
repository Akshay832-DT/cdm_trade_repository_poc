"""
FIX TradeOriginationDate field (tag 229).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeOriginationDateField(FIXFieldBase):
    """"""
    tag: str = "229"
    name: str = "TradeOriginationDate"
    type: str = "LOCALMKTDATE"
    value: date
