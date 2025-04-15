"""
FIX DeliveryDate field (tag 743).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DeliveryDateField(FIXFieldBase):
    """"""
    tag: str = "743"
    name: str = "DeliveryDate"
    type: str = "LOCALMKTDATE"
    value: date
