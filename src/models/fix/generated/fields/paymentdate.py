"""
FIX PaymentDate field (tag 504).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PaymentDateField(FIXFieldBase):
    """"""
    tag: str = "504"
    name: str = "PaymentDate"
    type: str = "LOCALMKTDATE"
    value: date
