"""
FIX PaymentRemitterID field (tag 505).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PaymentRemitterIDField(FIXFieldBase):
    """"""
    tag: str = "505"
    name: str = "PaymentRemitterID"
    type: str = "STRING"
    value: str
