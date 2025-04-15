"""
FIX PaymentRef field (tag 476).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PaymentRefField(FIXFieldBase):
    """"""
    tag: str = "476"
    name: str = "PaymentRef"
    type: str = "STRING"
    value: str
